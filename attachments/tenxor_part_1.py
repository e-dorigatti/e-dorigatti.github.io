from functools import reduce
import random
import math
from typing import Any, Callable, List, Optional, Sequence, Tuple


class Tenxor:
    def __init__(self, values: List[float], shape: Optional[List[int]]):
        self.values = values

        if shape is not None:
            # the total number of elements must equal the product
            # of the size of each dimension
            shape_elements = reduce(lambda x, y: x * y, shape)
            if len(values) != shape_elements:
                raise ValueError(
                    f"shape {shape} incompatible with values of size {len(values)}"
                )
            self._shape = shape
        else:
            self._shape = [len(self.values)]

    def get_shape(self) -> List[int]:
        return self._shape

    def __eq__(self, other: "Tenxor") -> bool:
        """
        Two Tenxors are the same if they have the same data and same shape.
        """
        return self._shape == other._shape and all(
            x == y for x, y in zip(self.values, other.values)
        )

    def __repr__(self):
        vals = ", ".join(map(str, self.values[:5]))
        return (
            f"{self.__class__.__name__} of {len(self.values)} items"
            f" with shape {self._shape} and values [{vals} ... ]"
        )


def ttransform(tenxor: Tenxor, op: Callable[[Any], Any]) -> Tenxor:
    """Transforms all elements of the Tenxor with the given callable."""
    return Tenxor([op(x) for x in tenxor.values], tenxor.get_shape())


def tmul_scalar(tenxor: Tenxor, scalar: float) -> Tenxor:
    """Multiplication by a scalar"""
    return ttransform(tenxor, lambda x: scalar * x)


def tadd_scalar(tenxor: Tenxor, scalar: float) -> Tenxor:
    """Addition with a scalar."""
    return ttransform(tenxor, lambda x: scalar + x)


def tview(old_shape: List[int], new_shape: List[int]) -> List[int]:
    """
    Return the new shape of the Tenxor after reshaping.
    """

    if any(s < -1 or s == 0 for s in new_shape):
        raise ValueError("Zero or negative shape other than -1 not allowed")

    # find if there is a dimension of size -1
    news = list(new_shape)
    fill_dimensions = [i for i, s in enumerate(new_shape) if s == -1]
    if len(fill_dimensions) > 1:
        raise ValueError("Only one dimension can be -1")
    elif fill_dimensions:
        # number of elements in the original tensor
        numel = reduce(lambda x, y: x * y, old_shape)

        # compute the total number of elements implied by the other dimensions
        other_ns = reduce(lambda x, y: x * y, (s for s in new_shape if s != -1))

        # this number must fit exactly into the total number of elements,
        # otherwise it is not possible to pack it into a single dimension
        if numel % other_ns != 0:
            raise ValueError(f"cannot reshape {old_shape} to {new_shape}")
        news[fill_dimensions[0]] = numel // other_ns

    return news


def tsqueeze(shape: List[int], dim: int) -> List[int]:
    """
    Return the new shape of the Tenxor after removing the given dimension of size 1.
    """

    if dim < 0:
        # support negative indexing from the end
        dim = len(shape) + dim

    # make sure that the dimension exists and has size 1
    if dim < 0 or dim > len(shape):
        raise ValueError("shape out of range")
    elif shape[dim] != 1:
        raise ValueError(f"cannot unsqueeze dimension {dim} of size {shape[dim]}")

    # simply remove the given dimension
    new_shape = [s for i, s in enumerate(shape) if i != dim]

    return new_shape


def tunsqueeze(shape: List[int], dim: int) -> List[int]:
    """
    Add a new dimension of size 1 in the given position.
    """

    if dim < 0:
        # support negative indexing from the end
        dim = len(shape) + dim + 1

    if dim < 0 or dim >= len(shape) + 1:
        # make sure that the dimension exists
        raise ValueError("shape out of range")

    # add a new dimension of size 1 in the right place
    new_shape = shape[:dim] + [1] + shape[dim:]

    return new_shape


def position_to_index(pos: List[int], shape: List[int]) -> int:
    """
    Find the index in the flattened array corresponding to the given
    position in the multi-dimensional tensor.
    """
    idx = 0
    acc = 1
    k = len(shape) - 1
    while k >= 0:
        if pos[k] >= shape[k]:
            raise RuntimeError(
                f"index {pos[k]} at dimension {k} out of bounds for size {shape[k]}"
            )
        idx += acc * pos[k]
        acc *= shape[k]
        k -= 1
    return idx


def index_to_position(idx: int, shape: List[int]) -> int:
    """
    Finds the position in the multi-dimensional tensor corresponding to
    the element at the given index in the flattened array.
    """

    # we could make this function more efficient by pre-computing this
    # and storing it in the Tenxor
    slice_sizes = [1] * len(shape)
    for k in range(len(shape) - 1, 0, -1):
        slice_sizes[k - 1] *= shape[k] * slice_sizes[k]

    pos = [0] * len(shape)
    for k in range(len(shape)):
        pos[k] = idx // slice_sizes[k]
        idx = idx % slice_sizes[k]

        if pos[k] >= shape[k]:
            raise RuntimeError(
                f"index {pos[k]} at position {k} out of bounds"
                f" for slice size {slice_sizes[k]}"
            )

    return pos


def next_position(pos: List[int], shape: List[int]) -> bool:
    """
    Find the multi-dimensional position immediately "after" the given position.
    Modifies `pos` in place, returns true if there are more elements to visit,
    or false if the computed position is out of bounds.
    """

    pos[-1] += 1
    k = len(pos) - 1
    while k > 0 and pos[k] == shape[k]:
        pos[k] = 0
        pos[k - 1] += 1
        k -= 1

    return pos[0] < shape[0]


class AbstractTenxor:
    # abstract interface
    def get_shape(self) -> List[int]:
        raise NotImplemented()

    def get_at_position(self, pos: List[int]) -> float:
        raise NotImplemented()

    def set_at_position(self, pos: List[int], val: float) -> None:
        raise NotImplemented()

    def next_position(self, pos: List[int]) -> bool:
        raise NotImplemented()

    def transform_values(self, op: Callable[[float], float]) -> "AbstractTenxor":
        raise NotImplemented()

    # shape features
    def squeeze(self, dim: int) -> "AbstractTenxor":
        new_shape = tsqueeze(self.get_shape(), dim)
        return self.view(new_shape)

    def unsqueeze(self, dim: int) -> "AbstractTenxor":
        new_shape = tunsqueeze(self.get_shape(), dim)
        return self.view(new_shape)

    def view(self, shape: List[int]) -> "AbstractTenxor":
        raise NotImplemented()


class Tenxor(AbstractTenxor):
    def __init__(self, values: List[float], shape: List[int]):
        self._values = values
        self._shape = shape

    def get_shape(self) -> List[int]:
        return self._shape

    def view(self, shape: List[int]) -> "Tenxor":
        return Tenxor(self._values, shape)

    def get_at_position(self, pos: List[int]) -> float:
        idx = position_to_index(pos, self._shape)
        return self._values[idx]

    def set_at_position(self, pos: List[int], val: float) -> None:
        idx = position_to_index(pos, self._shape)
        self._values[idx] = val

    def next_position(self, pos) -> bool:
        return next_position(pos, self._shape)

    def transform_values(self, op: Callable[[float], float]) -> "Tenxor":
        return Tenxor([op(x) for x in self._values], self._shape)

    def __eq__(self, other: "Tenxor") -> bool:
        return self._shape == other._shape and all(
            x == y for x, y in zip(self._values, other._values)
        )


def tredux(
    tenxor: AbstractTenxor, dim: int, init: Any, redux: Callable[[Any, Any], Any]
) -> AbstractTenxor:
    """
    Combine all elements of the given dimension using the operation provided.
    """

    if dim < 0:
        dim = len(tenxor.get_shape()) + dim
    if dim < 0 or dim > len(tenxor.get_shape()):
        raise ValueError("shape out of range")

    # Compute the shape of the result and initialize its elements.
    # At first we keep the dimension that we are reducing along, but with
    # only one element that contains the result along that slice.

    # initialize the result tensor
    res_shape = [s if i != dim else 1 for i, s in enumerate(tenxor.get_shape())]
    result = Tenxor([init] * reduce(lambda x, y: x * y, res_shape), res_shape)

    # initialize the counters
    res_pos = [0] * len(res_shape)
    res_has_more = True
    while res_has_more:
        # scan the input tensor along the given dimension and reduce all items there
        in_pos = res_pos[:]
        acc = init
        for i in range(tenxor.get_shape()[dim]):
            in_pos[dim] = i
            acc = redux(acc, tenxor.get_at_position(in_pos))
        result.set_at_position(res_pos, acc)

        # move to next result position
        res_has_more = result.next_position(res_pos)

    # finally remove the dimension that we reduced along
    return result.squeeze(dim)


def broadcast_shapes(
    shape_a: List[int], shape_b: List[int]
) -> Tuple[List[int], List[int], List[int]]:
    """
    Broadcast the shapes of two tensors, returning the new shapes after broadcasting as well
    as the shape of the result.
    """

    # match the length of the shapes by extending
    # the shorter one with ones to the left
    an, bn = len(shape_a), len(shape_b)
    if an == bn:
        pass
    elif an > bn:
        shape_b = [1] * (an - bn) + shape_b
    elif an < bn:
        shape_a = [1] * (bn - an) + shape_a

    # check that shapes are compabible, and compute the shape of the result
    result_shape = []
    for k, (n, m) in enumerate(zip(shape_a, shape_b)):
        r = None
        if n == 1:
            # dimension k of the first tensor is broadcasted
            # use dimension k of the second tensor as
            # size for this dimension of the result
            r = m
        elif m == 1:
            # dimension k of the second tensor is broadcasted
            # use dimension k of the first tensor as
            # size for this dimension of the result
            r = n
        elif m != n:
            # input tensors have different shapes that are not broadcastable,
            # i.e., different than one
            raise ValueError(
                f"incompatible shapes {shape_a} and {shape_b} at dimension {k}"
            )
        else:
            r = m

        result_shape.append(r)

    return shape_a, shape_b, result_shape


def tpoint(a: Tenxor, b: Tenxor, redux: Callable[[Any, Any], Any]) -> Tenxor:
    """
    Perform a pointwise operation by combining the two elements of the inputs
    that are in the same position after broadcasting.
    """

    # broadcast tensors and compute shape result
    a_shape, b_shape, result_shape = broadcast_shapes(a.get_shape(), b.get_shape())
    a_broad = a.view(a_shape)
    b_broad = b.view(b_shape)

    # initialize the container data for the result tensor and the position cursor
    result = Tenxor([None] * reduce(lambda m, n: m * n, result_shape), result_shape)
    result_pos = [0] * len(result_shape)
    result_has_more = True

    # perform the operation
    while result_has_more:
        # find the positions in the input arrays:
        # use 0 in each dimension that was broadcasted
        pos_a = [i if n > 1 else 0 for i, n in zip(result_pos, a_broad.get_shape())]
        pos_b = [i if n > 1 else 0 for i, n in zip(result_pos, b_broad.get_shape())]

        # perform the operation, store the result and move on
        res = redux(a_broad.get_at_position(pos_a), b_broad.get_at_position(pos_b))
        result.set_at_position(result_pos, res)
        result_has_more = result.next_position(result_pos)

    return result

