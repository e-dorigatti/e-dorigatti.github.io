---
layout: "post"
title: "Using large numpy arrays and pandas dataframes with multiprocessing"
date: 2020-06-19 09:00:00 +0200
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

print(f'Data size: {df.values.nbytes / 1024 / 204:.1f} MB')
df.iloc[:5, :5]
```

    Data size: 191.5 MB





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
      <td>0.851202</td>
      <td>0.541714</td>
      <td>0.723445</td>
      <td>0.735777</td>
      <td>0.283071</td>
    </tr>
    <tr>
      <th>Idx-1</th>
      <td>0.140121</td>
      <td>0.488509</td>
      <td>0.446370</td>
      <td>0.904190</td>
      <td>0.596619</td>
    </tr>
    <tr>
      <th>Idx-2</th>
      <td>0.118482</td>
      <td>0.022094</td>
      <td>0.637346</td>
      <td>0.675539</td>
      <td>0.496147</td>
    </tr>
    <tr>
      <th>Idx-3</th>
      <td>0.543767</td>
      <td>0.809873</td>
      <td>0.575806</td>
      <td>0.696533</td>
      <td>0.432091</td>
    </tr>
    <tr>
      <th>Idx-4</th>
      <td>0.242222</td>
      <td>0.244618</td>
      <td>0.947254</td>
      <td>0.871568</td>
      <td>0.436967</td>
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

    100%|██████████| 250/250 [00:17<00:00, 13.98it/s]


This is how you would naively transform this code to a parallel version using multiprocessing:


```python
with mp.Pool() as pool:
    tasks = ((df, df.index[idx]) for idx in process_rows)
    result = pool.imap(do_work, tasks)
    for res in tqdm(result, total=len(process_rows)):
        pass
```

    100%|██████████| 250/250 [01:37<00:00,  2.57it/s]


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
        
    def unlink(self):
        '''
        Releases the allocated memory. Call when finished using the data,
        or when the data was copied somewhere else.
        '''
        self._shared.close()
        self._shared.unlink()
```

Now, use this class to wrap the array, and send this wrapped object as parameter to a process and/or as a return value of the process, it's that simple! 

In particular, note that the array itself is not saved in the object. That is the whole point, we do not want to move it around! We can move the shared memory, though, because doing so will not copy the underlying memory, only a reference to it will be moved. Also note the `unlink` function: you must not forget to call it whenever you are done working with the array, or, alternatively, when you stored a copy somewhere else. If you don't do this, that shared memory will never be disposed of, and eventually you will run out of memory.

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
        
    def unlink(self):
        '''
        Releases the allocated memory. Call when finished using the data,
        or when the data was copied somewhere else.
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

    100%|██████████| 250/250 [00:13<00:00, 17.94it/s]


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

    100%|██████████| 24/24 [00:46<00:00,  1.93s/it]



```python
shared_df = SharedPandasDataFrame(df)

with mp.Pool() as pool:
    tasks = ((shared_df, df.index[idx]) for idx in process_rows)
    result = pool.imap(work_fast, tasks)
    for res in tqdm(result, total=len(process_rows)):
        res.unlink()  # IMPORTANT

shared_df.unlink()  # IMPORTANT
```

    100%|██████████| 24/24 [00:08<00:00,  2.83it/s]


Now that the computations take much longer than copying the result, the advantage becomes clearer.

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

    100%|██████████| 24/24 [00:09<00:00,  2.47it/s]


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


    100%|██████████| 24/24 [00:00<00:00, 10363.77it/s]


    Not shared


    100%|██████████| 24/24 [00:29<00:00,  1.21s/it]


Happy multiprocessing!

This blog post, by the way, is fully contained in a jupyter notebook downloadable from [here](/attachments/multiprocessing-large-objects.ipynb).
