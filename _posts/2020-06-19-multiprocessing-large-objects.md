---
layout: "post"
title: "Using large numpy arrays and pandas dataframes with multiprocessing"
date: 2020-06-19 09:00:00 +0200
categories: Python
---

Thanks to multiprocessing, it is relatively straightforward to write parallel
code in Python. However, these processes communicate by copying and
(de)serializing data, which can make parallel code even slower when large
objects are passed back and forth. This post shows how to use shared memory to
avoid all the copying and serializing, making it possible to have fast parallel
code that works with large datasets.

<!-- more -->

## The problem

In order to demonstrate the problem empirically, let us create a large data-frame and do some processing on each row:


```python
import multiprocessing as mp
import numpy as np
import pandas as pd
from tqdm import tqdm
```


```python
rows, cols = 1000, 5000
df = pd.DataFrame(
    np.random.random(size=(rows, cols)),
    columns=[f'Col-{i}' for i in range(cols)],
    index=[f'Idx-{i}' for i in range(rows)]
)

print(f'Data size: {df.values.nbytes / 1024 / 1204:.1f} MB')
df.iloc[:5, :5]
```

    Data size: 32.4 MB





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Col-0</th>
      <th>Col-1</th>
      <th>Col-2</th>
      <th>Col-3</th>
      <th>Col-4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Idx-0</th>
      <td>0.980677</td>
      <td>0.921510</td>
      <td>0.910434</td>
      <td>0.927914</td>
      <td>0.222692</td>
    </tr>
    <tr>
      <th>Idx-1</th>
      <td>0.320717</td>
      <td>0.412364</td>
      <td>0.007833</td>
      <td>0.874941</td>
      <td>0.121518</td>
    </tr>
    <tr>
      <th>Idx-2</th>
      <td>0.219621</td>
      <td>0.400342</td>
      <td>0.823636</td>
      <td>0.178868</td>
      <td>0.322418</td>
    </tr>
    <tr>
      <th>Idx-3</th>
      <td>0.577504</td>
      <td>0.622186</td>
      <td>0.218873</td>
      <td>0.142106</td>
      <td>0.871804</td>
    </tr>
    <tr>
      <th>Idx-4</th>
      <td>0.590041</td>
      <td>0.533683</td>
      <td>0.004371</td>
      <td>0.599954</td>
      <td>0.178846</td>
    </tr>
  </tbody>
</table>
</div>



Following is a simple, and a bit silly, row transformation: we construct a random matrix of the same size as the dataframe, take the mean across rows, and compute the outer product between it and the specified row. It is not too heavy computationally, but (this is the important part), both its inputs and outputs are matrices of size $1000\times5000$, which have five millions entries.


```python
def do_work(args):
    df, idx = args
    data = np.random.random(size=(len(df), len(df.columns)))
    result = np.outer(df.loc[idx], data.mean(axis=0))
    return result
```

We first set a baseline by transforming 250 random rows in a sequential fashion:


```python
process_rows = np.random.choice(len(df), 250)
for i in tqdm(process_rows):
    result = do_work((df, df.index[i]))
```

    100%|████████████████| 250/250 [00:16<00:00, 15.08it/s]


This is how you would naively transform this code to a parallel version using multiprocessing:


```python
with mp.Pool() as pool:
    tasks = ((df, df.index[idx]) for idx in process_rows)
    result = pool.imap(do_work, tasks)
    for res in tqdm(result, total=len(process_rows)):
        pass
```

    100%|████████████████| 250/250 [02:37<00:00,  1.58it/s]


This is much slower! As I hinted above, the problem is that the processes are exchanging a lot of data that has to be serialized, copied, and de-serialized. All of this takes time.

## The solution

Thansk to [`shared_memory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html), making this fast is a breeze! A caveat, though: it only works with Python 3.8 or above.

We are first going to deal with plain numpy arrays, then build upon this to share pandas dataframes. The idea is to write a wrapper that takes care of moving data to and from the shared memory. I strongly encourage you to read the documentation I linked above, which explains this in more detail.


```python
from multiprocessing.shared_memory import SharedMemory


class SharedNumpyArray:
    '''
    Wraps a numpy array so that it can be shared quickly among processes,
    avoiding unnecessary copying and (de)serializing.
    '''
    def __init__(self, array):
        '''
        Creates the shared memory and copies the array therein
        '''
        # create the shared memory location of the same size of the array
        self._shared = SharedMemory(create=True, size=array.nbytes)

        # save data type and shape, necessary to read the data correctly
        self._dtype, self._shape = array.dtype, array.shape

        # create a new numpy array that uses the shared memory we created.
        # at first, it is filled with zeros
        res = np.ndarray(
            self._shape, dtype=self._dtype, buffer=self._shared.buf
        )

        # copy data from the array to the shared memory. numpy will
        # take care of copying everything in the correct format
        res[:] = array[:]

    def read(self):
        '''
        Reads the array from the shared memory without unnecessary copying.
        '''
        # simply create an array of the correct shape and type,
        # using the shared memory location we created earlier
        return np.ndarray(self._shape, self._dtype, buffer=self._shared.buf)

    def copy(self):
        '''
        Returns a new copy of the array stored in shared memory.
        '''
        return np.copy(self.read_array())

    def close(self):
        '''
        Closes the shared memory. Call when this object will not
        be used anymore *in this process* (but it can still be used
        in other processes)
        '''
        self._shared.close()

    def unlink(self):
        '''
        Unlinks the shared memory. Call when this object will not be
        used anymore in any process.
        '''
        self._shared.unlink()
```

Now, use this class to wrap the array, and send this wrapped object as parameter to a process and/or as a return value of the process, it's that simple!

In particular, note that the array itself is not saved in the object. That is the whole point, we do not want to move it around! We can move the shared memory, though, because doing so will not copy the underlying memory, only a reference to it will be moved.

**A brief note on memory management:** as you can see, there is a `close` method and an `unlink` method: they must be used correctly so that the runtime can reclaim the memory used by objects that are not needed anymore. Failure of doing so will result in increasing memory usage over time, until no more free memory is available and the program will crash. How to avoid this? Briefly, every process has to `close` shared memory objects as soon as they are not needed anymore, and the last process *in addition* has to `unlink` it. See the producer-consumer example below for an example of this.

Using that wrapper, it is trivial to share a pandas dataframe: we wrap the values using the class above, and save index and columns.


```python
class SharedPandasDataFrame:
    '''
    Wraps a pandas dataframe so that it can be shared quickly among processes,
    avoiding unnecessary copying and (de)serializing.
    '''
    def __init__(self, df):
        '''
        Creates the shared memory and copies the dataframe therein
        '''
        self._values = SharedNumpyArray(df.values)
        self._index = df.index
        self._columns = df.columns

    def read(self):
        '''
        Reads the dataframe from the shared memory
        without unnecessary copying.
        '''
        return pd.DataFrame(
            self._values.read(),
            index=self._index,
            columns=self._columns
        )

    def copy(self):
        '''
        Returns a new copy of the dataframe stored in shared memory.
        '''
        return pd.DataFrame(
            self._values.copy(),
            index=self._index,
            columns=self._columns
        )

    def close(self):
        '''
        Closes the shared memory. Call when this object will not
        be used anymore *in this process* (but it can still be used
        in other processes)
        '''
        self._values.close()

    def unlink(self):
        '''
        Unlinks the shared memory. Call when this object will not be
        used anymore in any process.
        '''
        self._values.unlink()
```

Here is how to use them, and how quick it is:


```python
def work_fast(args):
    shared_df, idx = args

    # read dataframe from shared memory
    df = shared_df.read()

    # call old function
    result = do_work((df, idx))

    # wrap and return the result
    return SharedNumpyArray(result)
```


```python
shared_df = SharedPandasDataFrame(df)

with mp.Pool() as pool:
    tasks = ((shared_df, df.index[idx]) for idx in process_rows)
    result = pool.imap(work_fast, tasks)
    for res in tqdm(result, total=len(process_rows)):
        res.unlink()  # IMPORTANT

shared_df.unlink()  # IMPORTANT
```

    100%|████████████████| 250/250 [00:21<00:00, 11.50it/s]


Wait a minute! you might say, this is barely faster than the single-process version! Well yes, but it is roughly seven times faster than the multiprocessing version :). You might have noticed that there is still some copying going on, after all: when we create the shared memory, we have to copy the array in there. Depending on the computations you perform in the worker process, you might be able to avoid this, e.g. by pre-allocating the shared memory and performing only in-place operations, but it strongly depends on exactly what and how you compute.

The advantage of multiprocessing with shared memory becomes more apparent when workers perform more computations. For example, suppose we want to take the convolution of the whole dataframe with a $20\times20$ filter made by $20^2$ random entries of the specified row:


```python
from scipy.ndimage import convolve

def do_work(args):
    df, idx = args
    kernel_idx = np.random.choice(df.shape[1], 20 * 20)
    kernel = df.loc[idx][kernel_idx].values.reshape((20, 20))
    result = convolve(df.values, kernel)
    return result
```

As before, let us compare the sequential and multi-process versions. We can safely rule out the naive multiprocessing solution.


```python
process_rows = np.random.choice(len(df), 24)
for i in tqdm(process_rows):
    result = do_work((df, df.index[i]))
```

    100%|████████████████| 24/24 [01:01<00:00,  2.55s/it]



```python
shared_df = SharedPandasDataFrame(df)

with mp.Pool() as pool:
    tasks = ((shared_df, df.index[idx]) for idx in process_rows)
    result = pool.imap(work_fast, tasks)
    for res in tqdm(result, total=len(process_rows)):
        res.unlink()  # IMPORTANT

shared_df.unlink()  # IMPORTANT
```

    100%|████████████████| 24/24 [00:16<00:00,  1.43it/s]


Now that the computations take much longer than copying the result, the advantage becomes clearer.

## A producer-consumer example

Let's now consider the common scenario where we have several producer processes and one or more consumer processes. The idea here is that the producer processes do some work and create data, while consumer processes take this data and use it in some way. Consider for example the scenario described in a comment below, where we want to detect objects captured by several cameras, matching the same object among different cameras.

To start, let's create two functions to produce and consume things. In our example, the producer will capture a frame from a camera, run some object detection algorithm and extract [object descriptors](https://docs.opencv.org/3.4/df/d54/tutorial_py_features_meaning.html) for that frame. To keep things simple, I will simulate these descriptors with large random matrices, introducing some random artificial delay to simulate processing:


```python
import time
import random


def camera_capture():
    time.sleep(random.random())

    # 5000 descriptors with 250 features each
    return np.random.random(size=(5000, 250))
```

The consumer process will take object descriptors from all cameras and try to match them. To keep things simple, let's assume that matching can be done via the [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity), then we just need to compare the descriptors of all pairs of cameras:


```python
def object_matcher(frame, camera_objects):
    # cameras is a list of SharedNumpyArray's

    for i in range(len(camera_objects) - 1):
        if camera_objects[i] is None:
            continue

        for j in range(i + 1, len(camera_objects)):
            if camera_objects[j] is None:
                continue

            d1, d2 = camera_objects[i].read(), camera_objects[j].read()
            similarity = (d1 @ d2.T) / d1.shape[1]
            matches = np.sum(similarity > 0.4)
            if matches > 0:
                print('found', matches, 'matches at frame', frame, 'between cameras', i, 'and', j)
```

With these, we can now write the multiprocessing code. Generally, producer-consumer architectures make use of one or more [queues](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues) to share objects between processes. It is wise to limit the maximum size of the queue to a reasonable number of objects, so that in case the consumers are too slow compared to producers the computer's memory will not be filled up by objects waiting to be consumed.

The producer process will simply use `camera_capture` to "detect objects", wrap the descriptors into a `SharedNumpyArray` and put that into a queue. Most importantly, here we `close` the object descriptors after putting them into the queue as we will not use them anymore in this process.


```python
from queue import Full


# producer
def camera_process(camera_idx, queue):
    skips = 0

    # simulate 72 frames
    for i in range(72):
        objects = SharedNumpyArray(camera_capture())
        try:
            # timeout: how long to wait for a free spot in the queue
            queue.put((camera_idx, i, objects), block=True, timeout=2)
        except Full:
            # queue is still full after the timeout, skip frame and move on.
            # Note: these descriptors are now "lost" and won't be matched
            # print('full queue! camera', camera_idx, 'skipping frame', i)
            skips += 1
        finally:
            # *important:* always close the object as it is not needed anymore
            objects.close()

    print('camera', camera_idx, 'done capturing, skipped', skips, 'frames')
```

The consumer process will receive object descriptors from the queue and run the matcher algorithm above. We use a list to store the latest descriptors of each camera and free up memory of older descriptors as new ones come in. Note that we do that by using `close` followed by `unlink`. Also note that we consider a period of three seconds without receiving objects as a signal that producers are done capturing.


```python
from queue import Empty

# consumer
def matching_process(num_cams, queue):
    try:
        # here we store the latest descriptors
        camera_objects = [None] * num_cams

        while True:
            camera, frame, objects = queue.get(True, timeout=3)

            # free memory of old descriptors
            if camera_objects[camera] is not None:
                camera_objects[camera].close()
                camera_objects[camera].unlink()

            # store latest descriptors
            camera_objects[camera] = objects

            # match every 8 frames because
            # exhaustive matching every frame is too slow
            if frame % 8 == 0:
                object_matcher(frame, camera_objects)

    except Empty:
        # empty queue, matching process quitting
        pass

    print('matcher quitting')

    # release all memory
    for c in camera_objects:
        if c is not None:
            c.close()
            c.unlink()
```

We can finally weave these processes together and start the game!


```python
num_cameras = 5
num_matchers = 2

start_time = time.time()

# create queue
queue = mp.Queue(maxsize=num_cameras * 10)

# start consumer processes
matchers = []
for i in range(num_matchers):
    m = mp.Process(target=matching_process, args=(num_cameras, queue))
    m.start()
    matchers.append(m)
    print('started matcher', i + 1)

# start producer processes
cams = []
for i in range(num_cameras):
    c = mp.Process(target=camera_process, args=(i, queue))
    c.start()
    cams.append(c)
    print('started camera', i + 1)

print('capturing and matching in progress ...')

# wait for all processes to quit
for c in cams:
    c.join()
for m in matchers:
    m.join()
queue.close()

print('capturing completed')

end_time = time.time()
print('total time taken:', end_time - start_time)
```

    started matcher 1
    started matcher 2
    started camera 1
    started camera 2
    started camera 3
    started camera 4
    started camera 5
    capturing and matching in progress ...
    found 2 matches at frame 0 between cameras 3 and 4
    found 2 matches at frame 0 between cameras 2 and 3
    found 1 matches at frame 0 between cameras 0 and 3
    found 2 matches at frame 0 between cameras 2 and 4
    found 2 matches at frame 0 between cameras 3 and 4
    found 5 matches at frame 8 between cameras 0 and 2
    found 2 matches at frame 8 between cameras 2 and 3
    found 5 matches at frame 8 between cameras 0 and 4
    found 3 matches at frame 16 between cameras 1 and 3
    found 3 matches at frame 24 between cameras 3 and 4
    found 3 matches at frame 56 between cameras 0 and 3
    found 2 matches at frame 40 between cameras 1 and 2
    camera 2 done capturing, skipped 5 frames
    found 2 matches at frame 48 between cameras 1 and 2
    camera 1 done capturing, skipped 6 frames
    found 2 matches at frame 64 between cameras 0 and 3
    camera 3 done capturing, skipped 7 frames
    camera 0 done capturing, skipped 5 frames
    camera 4 done capturing, skipped 5 frames
    found 1 matches at frame 56 between cameras 1 and 2
    found 2 matches at frame 64 between cameras 2 and 3
    matcher quitting
    matcher quitting
    capturing completed
    total time taken: 77.68669128417969


I hope this skeleton will be helpful in your application!

## When is this solution (not) applicable?

As discussed above, there is still some copying involved, therefore it is not straightforward to tell when this solution might be faster. When the size of the result is large, but the computations required to obtain it are not so heavy, a sequential approach might be faster, but it is not clear where to draw the line.

Another case to watch out is when you have large inputs, but small outputs. This solution is not necessary when you only read the input, but do not modify it. This is because the inputs follow a mechanism called [copy-on-write](https://en.wikipedia.org/wiki/Copy-on-write), i.e. are not copied _unless_ they are modified. This can be shown by slightly modifying the example above to return the sum of the convolution, instead of the convolution itself:


```python
def do_work(args):
    df, idx = args
    kernel_idx = np.random.choice(df.shape[1], 20 * 20)
    kernel = df.loc[idx][kernel_idx].values.reshape((20, 20))
    result = convolve(df.values, kernel)
    return result.sum()


with mp.Pool() as pool:
    tasks = ((df, df.index[idx]) for idx in process_rows)
    result = pool.imap(do_work, tasks)
    for res in tqdm(result, total=len(process_rows)):
        pass
```

    100%|████████████████| 24/24 [00:17<00:00,  1.35it/s]


This is now as fast as the code above returning the whole result of the convolution.

However, if you have classes the trick above becomes necessary again. I honestly do not know why. This also happens if the worker function is defined outside of the class.


```python
class Worker:
    def __init__(self):
        self.data = np.random.random(size=(10000, 10000))

    @staticmethod
    def work_not_shared(args):
        data, i = args
        return data[i].mean()

    def run_not_shared(self):
        with mp.Pool() as pool:
            tasks = [[self.data, idx] for idx in range(24)]
            result = pool.imap(self.work_not_shared, tasks)
            for res in tqdm(result, total=len(tasks)):
                pass

    @staticmethod
    def work_shared(args):
        data, i = args
        return data.read()[i].mean()

    def run_shared(self):
        shared = SharedNumpyArray(self.data)
        with mp.Pool() as pool:
            tasks = [[shared, idx] for idx in range(24)]
            result = pool.imap(self.work_shared, tasks)
            for res in tqdm(result, total=len(tasks)):
                pass
        shared.unlink()


print('Shared')
Worker().run_shared()

print('Not shared')
Worker().run_not_shared()
```

    Shared


    100%|████████████████| 24/24 [00:00<00:00, 181049.09it/s]


    Not shared


    100%|████████████████| 24/24 [00:41<00:00,  1.74s/it]


Happy multiprocessing!

This blog post, by the way, is fully contained in a jupyter notebook downloadable from [here](/attachments/multiprocessing-large-objects.ipynb).
