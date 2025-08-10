---
date: 2025-08-18 00:00:00 +0200
title: " Tensor computing from scratch part II - Advanced operations"
layout: post
categories:
 - Deep Learning
 - Python
 - Math
 - Development
---

Welcome back to the "tensor computing from scratch" series, where we re-implement pytorch from first principles!

In the <a href="{% post_url 2025-01-17-tenxor-computing-part-1 %}">first part</a> we have seen how to create a basic data container and perform two fundamental operations, namely reductions along one axis and pointwise operations between two tensors, including shape braodcasting.
While what we wrote so far is already pretty freakin' cool, if you ask me, it is rather bare-bones and still missing some important features.

<!-- more -->

Let's recap what we did in the <a href="{% post_url 2025-01-17-tenxor-computing-part-1 %}"> first part</a>:
  - We created the `Tenxor` class, containing all data in a simple list and remembering the shape of the tensor.
  - We then wrote functions `position_to_index` and `index_to_position` that convert between tensor coordinates and index in the list.
  - We also wrote `next_position` computing the tensor coordinates corresponding to the item in the list with index immediately following a given index.
    This makes it very easy to work with tensors of arbitrary shape by visiting one item at a time.
  - We then used these functions to write `tredux` which aggregates all elements in a given dimension, for example by computing their sum.
    This is one of the core operations of our tensor library.
  - The second core operation is `tpoint`, which combines two tensors by matching elements at corresponding positions.
    The real power of this function is to efficiently handle tensors of different shapes through [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html).
  - Broadcasting and correspondence between different shapes was established by the function `broadcast_shapes`.
  - The last core operation is `ttransform` which transforms each item in the tensor independently, for example by negating it;
  - Finally, we wrote the function `tview` that changes the shape of a tensor, and we specialized it into `tsqueeze` and `tunsqueeze` that respectively remove and add dimensions of size 1. Since the tensor data is stored in a simple list, all these functions do is simply to save the new shape after performing a few basic consistency checks.

We then added these functions to a base tensor class:

```python
class AbstractTenxor:
    def get_shape(self) -> List[int]:
        ...

    def get_at_position(self, pos: List[int]) -> float:
        ...

    def set_at_position(self, pos: List[int], val: float) -> None:
        ...

    def next_position(self, pos: List[int]) -> bool:
        ...

    def transform_values(self, op: Callable[[float], float]) -> "AbstractTenxor":
        ...

    def squeeze(self, dim: int) -> "AbstractTenxor":
        ...

    def unsqueeze(self, dim: int) -> "AbstractTenxor":
        ...

    def view(self, shape: List[int]) -> "AbstractTenxor":
        ...
```

These functions are already comprehensive enough to support a wide variety of operations with tensors, but two conspicuous features are missing: swapping axes positions (that is, the generic version of matrix transpose), and indexing of sub-tensors.
Both of these are complex enough that we need to rewrite and generalize most of the code we wrote eariler.


## Pretty printing tensors

Before starting the dirty work, let's warm up by writing a function to "pretty print" data in a tensor.

Let's start by importing some basic libraries and <a href="/attachments/tenxor_part_1.py">the code</a> we wrote in <a href="{% post_url 2025-01-17-tenxor-computing-part-1 %}">part I</a>.

```python
import random
import math
from typing import Any, Callable, List, Optional, Sequence, Tuple
from functools import reduce

from tenxor_part_1 import *
```

Since we now have the freedom to do things in whatever way we like, let's try to improve the way tensors are printed compared to the defaults by numpy and pytorch:

```python
def tenxor_to_string(t: Tenxor, dims: Optional[Sequence[int]] = None) -> str:
    """
    Prints the elements of the tensor across the given slice
    use `None` to print all items of that dimension,
    otherwise specify an index to only print items at
    that position
    """

    if dims is None:
        dims = [None] * len(t.get_shape())

    cursor = []  # current position in the tenxor
    slice_dims = []  # dimensions that span the slice we want to print
    for i, p in enumerate(dims):
        if p is None:
            cursor.append(0)
            slice_dims.append(i)
        else:
            cursor.append(p)

    rep = []
    has_more = True
    while has_more:
        rep.append("%7.2f  " % t.get_at_position(cursor))

        # find the next item that we need to print
        # this is similar to next_position in part 1,
        # except that this time we can only move
        # in a restricted set of dimensions
        # (i.e., those that we want to print)
        k = len(slice_dims) - 1
        cursor[slice_dims[k]] += 1
        while k > 0 and cursor[slice_dims[k]] >= t.get_shape()[slice_dims[k]]:
            cursor[slice_dims[k]] = 0
            cursor[slice_dims[k - 1]] += 1
            k -= 1

        has_more = cursor[slice_dims[0]] < t.get_shape()[slice_dims[0]]

        # print an appropriate separator if we reached the end
        # of a dimension (newline for rows, dashes for 2D slices,
        # equal signs for  3D slices, etc.)
        if has_more and k != len(slice_dims) - 1:
            sep_idx = len(slice_dims) - k - 2
            rep.append([
                "\n", "\n---\n", "\n===\n", "\n***\n", "\n###\n"
            ][sep_idx])

    rep.append("\n")
    return "".join(rep)


def tprint(t: Tenxor, dims: Optional[Sequence[int]] = None) -> str:
    print(tenxor_to_string(t, dims))


# print all items whose first index is 3
# in python notation, that would be tenxor[3, :, :, :]
tprint(
    Tenxor(list(range(4**5)), shape=[4, 2, 2, 4, 4]),
    (3, None, None, None, None)
)
```

     192.00   193.00   194.00   195.00  
     196.00   197.00   198.00   199.00  
     200.00   201.00   202.00   203.00  
     204.00   205.00   206.00   207.00  
    ---
     208.00   209.00   210.00   211.00  
     212.00   213.00   214.00   215.00  
     216.00   217.00   218.00   219.00  
     220.00   221.00   222.00   223.00  
    ===
     224.00   225.00   226.00   227.00  
     228.00   229.00   230.00   231.00  
     232.00   233.00   234.00   235.00  
     236.00   237.00   238.00   239.00  
    ---
     240.00   241.00   242.00   243.00  
     244.00   245.00   246.00   247.00  
     248.00   249.00   250.00   251.00  
     252.00   253.00   254.00   255.00  
    


The data printed above represents a tensor of shape (2, 2, 4, 4).
The last two dimensions are printed as normal 4x4 matrices, and higher order "slices" are separated by different separators depending on their rank.
There are two pairs of 4x4 matrices (that is, two tensors tensor of shape 2x4x4) separated by `===`, and each matrix in the pair is separated by `---`.
Within each pair, the two matrices are stacked into a cube, and the two cubes are stacked into a 4-dimensional hypercube.

Sometimes I wish numpy and pytorch printed tensors in this way... ;)

## Axis re-ordering

Back to math, a fundamental feature that we are missing is the ability to re-order axes.
This operation is what allows us to transpose matrices.

As of now, all our functions operate with the assumption that the last dimension is the first one to change when we move in the data list, then the second-to-last, etc.
The central idea is then to override this logic and allow an user-defined axis ordering.
We will use a tuple with the same number of items as the tensor shape, each element in the tuple indicating the order in which the corresponding axis is supposed to change.
For example, the default order for a three-dimensional tensor would be `(2, 1, 0)`, meaning that the last dimension is the first to change, the second-to-last dimension is the second to change, etc.
In this way, transposing the last two dimensions would simply mean using `(2, 0, 1)` as axis order.

The first way I tried to implement this was to modify `position_to_index`, `index_to_position` and `next_position` to accept the axis order as an additional parameter, and navigate the tensor accordingly.
While this worked fine, it then made things considerably more complicated later on when I wanted to add indexing as an additional feature, as it created a large number of edge-cases that were difficult to handle cleanly.

Therefore, to avoid this complexity, we are going to create a new tensor class that encapsulates another tensor permuting its axes in a desired order:

```python
class TransposedTenxor(AbstractTenxor):
    def __init__(self, wrapped: AbstractTenxor, axis_order: List[int]):
        self._wrapped = wrapped

        # the given order should contain a permutation
        # of the numbers 0, ..., len(shape) - 1
        if len(axis_order) != len(wrapped.get_shape()) or set(axis_order) != set(
            range(len(wrapped.get_shape()))
        ):
            raise ValueError(
                f"given axis order {axis_order} incompatible"
                f"with shape {self._wrapped.get_shape()}"
            )
        self._axis_order = axis_order

    def get_shape(self) -> List[int]:
        shape = self._wrapped.get_shape()
        return [shape[i] for i in self._axis_order]

    def get_at_position(self, pos: List[int]) -> float:
        return self._wrapped.get_at_position([pos[i] for i in self._axis_order])

    def set_at_position(self, pos: List[int], val: float) -> None:
        self._wrapped.set_at_position([pos[i] for i in self._axis_order], val)

    def next_position(self, pos: List[int]) -> bool:
        return next_position(pos, self.get_shape())

    def transform_values(self, op: Callable[[float], float]) -> AbstractTenxor:
        return self._wrapped.transform_values(op)
```

And two related utility methods: 


```python
def tswapaxes(tenxor: AbstractTenxor, ax1: int, ax2: int):
    """Swaps the two given axes of a tensor."""
    order = list(range(len(tenxor.get_shape())))
    order[ax1], order[ax2] = order[ax2], order[ax1]
    return TransposedTenxor(tenxor, order)


def ttranspose(tenxor: AbstractTenxor):
    """Transposes the tensor, i.e., swaps the last two axes."""
    return tswapaxes(tenxor, -1, -2)
```


```python
tw = Tenxor([1, 2, 3, 4, 5, 6], shape=[2, 3])
tprint(tw)
```

       1.00     2.00     3.00  
       4.00     5.00     6.00  
    



```python
tt = ttranspose(tw)
tprint(tt)
```

       1.00     4.00  
       2.00     5.00  
       3.00     6.00  
    


Transposing a transpose should result in the original tensor:


```python
ttt = ttranspose(tt)
tprint(ttt)
```

       1.00     2.00     3.00  
       4.00     5.00     6.00  
    


Note that these three tensors all share the same memory storage, but they interpret it in different ways!

## Reshaping redefined

The implementation of reshaping that we introduced in part one is easy enough, we simply overwrite the old shape with the new shape and everything works out of the box.
Unfortunately, this does not work anymore with our transposed tensor implementation.

To support generic reshaping, we apply the same trick that we used to swap axes: we will provide a "translation" layer that will match locations before and after reshaping.
This conversion is actually quite simple. Consider the same element in the flattened storage; In part one, we saw how to find the multi-dimensional index of this element given the shape of the tensor.
If we now have two views with different shapes, this element in the flattened array will go in different locations as determined by the shapes of the two views.
So, because the two locations refer to the same storage element, we can convert from one to the other by finding the offset in the storage, and converting this offset into the location with respect to the other tensor.
It's a mouthful in English, but very simple in code:


```python
def view_position_to_original_position(
    view_pos: List[int], view_shape: List[int], original_shape: List[int]
) -> List[int]:
    """Converts the position of an element in a reshaped tensor
    to the position of the same element in the original tensor.
    """

    offset = position_to_index(view_pos, view_shape)
    pos = index_to_position(offset, original_shape)
    return pos


# element (0, 1) of a (3, 2) tensor corresponds to element (1,) in a (6,) tensor
assert view_position_to_original_position([0, 1], [3, 2], [6]) == [1]

# element (2, 1) of a (3, 2) tensor corresponds to element (5,) in a (6,) tensor
assert view_position_to_original_position([2, 1], [3, 2], [6]) == [5]
```

Here's the wrapper that uses this function:


```python
class ReshapedTenxor(AbstractTenxor):
    def __init__(self, wrapped: AbstractTenxor, shape: List[int]):
        self._wrapped = wrapped
        self._shape = shape

    def get_shape(self) -> List[int]:
        return self._shape

    def get_at_position(self, pos: List[int]) -> float:
        pos = view_position_to_original_position(
            pos, self._shape, self._wrapped.get_shape()
        )
        return self._wrapped.get_at_position(pos)

    def set_at_position(self, pos: List[int], val: float) -> None:
        pos = view_position_to_original_position(
            pos, self._shape, self._wrapped.get_shape()
        )
        self._wrapped.set_at_position(pos, val)

    def next_position(self, pos) -> bool:
        return next_position(pos, self._shape)

    def transform_values(self, op: Callable[[float], float]) -> "Tenxor":
        return self._wrapped.transform_values(op)
```

And here's a small test following the small example above:


```python
t = Tenxor(list(range(6)), [6])
tprint(t)
```

       0.00     1.00     2.00     3.00     4.00     5.00  
    



```python
tprint(ReshapedTenxor(t, [2, 3]))
```

       0.00     1.00     2.00  
       3.00     4.00     5.00  
    



```python
tprint(ReshapedTenxor(t, [3, 2]))
```

       0.00     1.00  
       2.00     3.00  
       4.00     5.00  
    



```python
tprint(ReshapedTenxor(t, [6, 1]))
```

       0.00  
       1.00  
       2.00  
       3.00  
       4.00  
       5.00  
    


## Indexing

The last major feature we need to support is indexing items or entire slices of a tensor, i.e., we want to write code like `matrix[2:5, 1:-1]` to take rows 2, 3 and 4 all columns but the first and last.
And, as usual, we want to do this efficiently, i.e., without creating a new copy of the underlying data storage.

We will offer several ways to subset each dimension:
 - A `None` means that we do not subset that axis;
 - An `int` means that we only take the slice with the specified index;
 - A `List[int]` means that we take all slices with those indices;
 - A generic `slice` object allows us to consider arbitrary expressions like `20:5:-3`.

As before, we will create a wrapper that will redirect the index location to the correct position of the wrapped tensor.
The first thing to implement is to use these specifications to compute the final shape of the sliced tensor:


```python
Slice = slice | List[int] | int | None


def compute_sliced_shape(full_shape: List[int], slices: List[Slice]) -> List[int]:
    """Computes the shape that results from slicing a tensor of the given shape."""

    if len(slices) > len(full_shape):
        raise RuntimeError("specify at most one slice per dimension")
    elif len(slices) < len(full_shape):
        slices = slices + [None] * (len(full_shape) - len(slices))

    new_shape = []
    for dim, sli in zip(full_shape, slices):
        # find out how many items we take of this axis
        if sli is None:
            # no slicing here
            new_shape.append(dim)
        elif isinstance(sli, int):
            # only take a single element
            new_shape.append(1)
        elif isinstance(sli, list):
            # take a subset of elements
            new_shape.append(len(sli))
        elif isinstance(sli, slice):
            # find how many slices we need to take
            start, stop, step = sli.indices(dim)
            count = math.ceil((stop - start) / step)
            new_shape.append(count)
        else:
            raise RuntimeError("unsupported slicing specification")

    return new_shape


assert compute_sliced_shape(
    [5, 4, 3],
    # take 3rd and 4th of the first dimension, all of the second,
    # and 2nd of third dimension
    [[2, 3], None, 1],
) == [2, 4, 1]

assert compute_sliced_shape(
    [5, 4, 3],
    # take 4th of the 1st dimension, and everything else
    [3],
) == [1, 4, 3]

assert compute_sliced_shape(
    [5, 4, 3],
    # take everything of the 1st dimension, 4th and 3rd of second dimension,
    # and everything else
    [None, slice(3, 1, -1)],
) == [5, 2, 3]
```

The next step is to translate positions in the sliced tensor back to the position in the full tensor:


```python
def sliced_position_to_full_position(
    pos: List[int], full_shape: List[int], slices: List[slice]
) -> List[int]:
    """Converts the position of an element in a sliced tensor to the
    position of that element in the original tensor.
    """
    if len(slices) > len(full_shape):
        raise RuntimeError("specify at most one slice per dimension")
    elif len(slices) < len(full_shape):
        slices = slices + [None] * (len(full_shape) - len(slices))

    full_pos = []
    for idx, dim, sli in zip(pos, full_shape, slices):
        if sli is None:
            # no slicing here, the index did not change
            full_pos.append(idx)
        elif isinstance(sli, int):
            # only one dimension was taken
            # the index in the implied shape must be 0
            # and the index in the full shape is the slice that was taken
            if idx != 0:
                raise RuntimeError("out of bounds")
            full_pos.append(sli)
        elif isinstance(sli, list):
            # a subset of elements was taken
            # use the provided list to map indices back
            full_pos.append(sli[idx])
        elif isinstance(sli, slice):
            # compute which index was taken
            start, stop, step = sli.indices(dim)
            count = math.ceil((stop - start) / step)
            if idx >= count:
                raise RuntimeError("out of bounds")
            full_pos.append(start + step * idx)
        else:
            raise RuntimeError("unsupported slicing specification")

    return full_pos
```

Let's create a test example:


```python
full_shape = [5, 2, 3]
slices = [
    [3, 4],  # 4th and 5th of first dimension
    None,  # all of second dimension
    slice(3, 0, -1),  # 3rd and 2nd of 3rd dimension (index 3 is out-of-bounds)
]
subset_shape = compute_sliced_shape(full_shape, slices)
subset_shape
```




    [2, 2, 2]



Now we navigate across all elements of the sliced tensor, and check that they are mapped to the correct position of the original tensor:


```python
subset_pos = [0, 0, 0]
has_more = True
while has_more:
    full_pos = sliced_position_to_full_position(subset_pos, full_shape, slices)
    print(f"position {subset_pos} maps to {full_pos}")
    has_more = next_position(subset_pos, subset_shape)
```

    position [0, 0, 0] maps to [3, 0, 2]
    position [0, 0, 1] maps to [3, 0, 1]
    position [0, 1, 0] maps to [3, 1, 2]
    position [0, 1, 1] maps to [3, 1, 1]
    position [1, 0, 0] maps to [4, 0, 2]
    position [1, 0, 1] maps to [4, 0, 1]
    position [1, 1, 0] maps to [4, 1, 2]
    position [1, 1, 1] maps to [4, 1, 1]


Note how this also handles moving backwards. Neat!

Last, let's create the wrapper:


```python
class SlicedTenxor(AbstractTenxor):
    def __init__(self, wrapped: Tenxor, slices: List[Slice]):
        self._wrapped = wrapped
        self._slices = slices
        self._shape = compute_sliced_shape(self._wrapped.get_shape(), self._slices)

    def position_to_index(self, pos: List[int]) -> int:
        return position_to_index(pos, self._shape)

    def index_to_position(self, idx: int) -> List[int]:
        return index_to_position(idx, self._shape)

    def get_shape(self) -> List[int]:
        return self._shape

    def get_at_position(self, pos: List[int]) -> float:
        full_pos = sliced_position_to_full_position(
            pos, self._wrapped.get_shape(), self._slices
        )
        return self._wrapped.get_at_position(full_pos)

    def set_at_position(self, pos: List[int], val: float) -> None:
        full_pos = sliced_position_to_full_position(
            pos, self._wrapped.get_shape(), self._slices
        )
        self._wrapped.set_at_position(full_pos, val)

    def next_position(self, pos: List[int]) -> bool:
        return next_position(pos, self.get_shape())

    def transform_values(self, op: Callable[[float], float]) -> "AbstractTenxor":
        return self._wrapped.transform_values(op)
```

## Putting everything together

In terms of features, our small library is already quite advanced!
But it is also quite cumbersome to use.
Therefore, before applying our tensor library to a real use-case, let's write a few simple utilities to make our life simpler.


```python
global_rng = random.Random(123)


def trandom(*shape: int, seed: Optional[int] = None) -> Tenxor:
    """
    Create a tensor with the given shape and elements sampled randomly in [-1, 1]
    """
    numel = reduce(lambda x, y: x * y, shape)

    rng = global_rng if seed is None else random.Random(seed)
    return Tenxor([2 * rng.random() - 1 for _ in range(numel)], shape=list(shape))


def tadd(a: Tenxor, b: Tenxor) -> Tenxor:
    """Pointwise addition of two tensors"""
    return tpoint(a, b, lambda x, y: x + y)


def tmul(a: Tenxor, b: Tenxor) -> Tenxor:
    """Pointwise multiplication of two tensors"""
    return tpoint(a, b, lambda x, y: x * y)


def tdiv(a: Tenxor, b: Tenxor) -> Tenxor:
    """Pointwise division of two tensors"""
    return tpoint(a, b, lambda x, y: x / y)


def tsum(a: Tenxor, dim: int) -> Tenxor:
    """Sum reduction across the given dimension"""
    return tredux(a, dim, 0, lambda x, y: x + y)


def tmean(a: Tenxor, dim: int) -> Tenxor:
    """Mean reduction across the given dimension"""
    return tredux(a, dim, 0, lambda x, y: (x + y) / a.get_shape()[dim])
```

With these, let's create something more exciting, such as a batched matrix multiplication:


```python
def tmatmul(a: Tenxor, b: Tenxor) -> Tenxor:
    """matrix multiplication along the two rightmost dimensions"""

    # tmp[..., i, k, j] = a[..., i, k, 1] * b[..., 1, k, j]
    tmp = tmul(a.unsqueeze(-1), b.unsqueeze(-3))

    # res[..., i, j] = sum_k ( tmp[..., i, k, j] )
    res = tsum(tmp, -2)

    return res


assert tmatmul(
    Tenxor([1, 2, 3, 2, 4, 6], [2, 3]),
    Tenxor([1, 4, 2, 5, 3, 6], [3, 2]),
) == Tenxor([14, 32, 28, 64], shape=[2, 2])
```

To create a more comfortable user interface, let's hide all these helper methods into the base tensor class:


```python
AbstractTenxor.print = tprint
AbstractTenxor.view = lambda t, s: ReshapedTenxor(t, s)
AbstractTenxor.t = ttranspose
AbstractTenxor.swapaxes = tswapaxes
AbstractTenxor.slice = lambda t, s: SlicedTenxor(t, s)
AbstractTenxor.__getitem__ = AbstractTenxor.slice
AbstractTenxor.__repr__ = Tenxor.__repr__ = tenxor_to_string
AbstractTenxor.add = tadd
AbstractTenxor.add_scalar = tadd_scalar
AbstractTenxor.mul = tmul
AbstractTenxor.mul_scalar = tmul_scalar
AbstractTenxor.div = tdiv
AbstractTenxor.sum = tsum
AbstractTenxor.mean = tmean
AbstractTenxor.matmul = tmatmul
```

And now, let's try to combine everything we've done so far in a pointlessly convoluted example!


```python
t1 = Tenxor(list(range(20)), [4, 5])
t1
```




       0.00     1.00     2.00     3.00     4.00  
       5.00     6.00     7.00     8.00     9.00  
      10.00    11.00    12.00    13.00    14.00  
      15.00    16.00    17.00    18.00    19.00  




```python
a = t1.slice([[1, 3], slice(0, 5, 2)])
a
```




       5.00     7.00     9.00  
      15.00    17.00    19.00  




```python
at = a.t()
at
```




       5.00    15.00  
       7.00    17.00  
       9.00    19.00  



Note that our implementation also allows to duplicate dimensions, isn't that cool?


```python
b = t1.slice([[1, 1], slice(4)])
b
```




       5.00     6.00     7.00     8.00  
       5.00     6.00     7.00     8.00  




```python
bt = b.swapaxes(0, 1)
bt
```




       5.00     5.00  
       6.00     6.00  
       7.00     7.00  
       8.00     8.00  




```python
tr = at.matmul(bt.view([2, 4]))
tr
```




     130.00   130.00   150.00   150.00  
     154.00   154.00   178.00   178.00  
     178.00   178.00   206.00   206.00  



I have no idea what the result of all of this is supposed to be, but it didn't crash so I count it as a success :)

Stay tuned for part 3, where we are going to put this library to the test by implementing a graph neural network!
