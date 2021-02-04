---
layout: post
title:  "Temporary variables in Python's list comprehension"
date: 2021-02-05 09:00:00 +0200
---

Although list comprehensions are very handy, it is difficult to write
non-trivial expressions, mostly because it is not possible to use variables to
store temporary results. Or is it?

<!-- more -->

Consider a somewhat silly example:

```{python}
[
    2 * x
    for x in range(10)
    if x % 2 == 0 and 2 * x % 8 == 0
]
```

Here, we are filtering elements of an iterable, applying a transformation, and
filtering the result. In particular, note that we are writing the transformation
twice: when filtering, and when computing the result. Can we avoid this
repetition?

Turns out it's possible with a simple trick: put the transformed item into a
list and use a nested comprehension:


```{python}
[
    y
    for x in range(10)
    if x % 2 == 0
    for y in [2 * x]
    if y % 8 == 0
]
```

This trick is straightforward to apply to multiple transformations and
conditions, so that each step has access to the variables defined (and filtered)
earlier:

```{python}
[
    process(each, tmp1, tmp2, tmp3)
    for each in lst
    if cond(each)
    for tmp1 [ compute_tmp1(each) ]
    if cond1(tmp1)
    for tmp2 [ compute_tmp2(each, tmp1) ]
    if cond2(tmp1, tmp2)
    for tmp3 [ compute_tmp3(each, tmp1, tmp2) ]
    if cond3(tmp1, tmp2, tmp3)
]
```

I leave it to you to decide whether this is a good idea in "serious" code. It's
uncommon enough to trigger a WTF in pretty much everybody reading this for the
first time.

![](https://mk0osnewswb2dmu4h0a.kinstacdn.com/images/comics/wtfm.jpg){: .center-image }
