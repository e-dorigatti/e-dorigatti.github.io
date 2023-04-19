---
layout: post
title: "Temporary variables in Python"
date: 2023-04-19 12:00:00 +0200
categories:
 - Python
---

Very easy using context managers!

<!-- more -->


The functions `locals()` and `globals()` return dictionaries containing the
variables that are defined in the current local or global scope. What is cool is
that variables can be declared, modified, and "undeclared" by modifying these
dictionaries (see a tutorial [here][plg])!

To get a temporary variable, we can therefore build a [context manager][ctx]
that adds and removes a variable to either the local or the global definitions,
for example:

 [plg]: https://www.tutorialsteacher.com/articles/globals-and-locals-in-python
 [ctx]: https://docs.python.org/3/reference/datamodel.html#context-managers



```python
class TemporaryVariables:
    def __init__(self, dest, **kwargs):
        # dest is a dictionary, either from locals() or globals()
        # kwargs are the variables to define, and their values
        self._vars = kwargs
        self._old = dest
        self._backup = {}
        for k, v in self._vars.items():
            # for each variable...
            if k in self._old:
                # store the old value if overwriting
                self._backup[k] = self._old[k]
            # and set the new value
            self._old[k] = v

    def __enter__(self, *args, **kwargs):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        for k, v in self._vars.items():
            # for each variable...
            if k in self._backup:
                # restore the old value if it was overwritten
                self._old[k] = self._backup[k]
            else:
                # or "undefine" the variable if it was new
                self._old.pop(k)
```

Here's how you would use this:


```python
a = 'hello'
print(a)
with TemporaryVariables(locals(), a='world'):
    a = a + '!'
    print(a)
print(a)
```

Which prints:

```
hello
world!
hello
```


Due to the way we took the backup, variables that were not defined before the
`with` block remain undefined after it, too:


```python
with TemporaryVariables(locals(), x=42):
    print(x)
print(x)  # x was only defined in the with block
```

We now get an error when using `x` after whe `with`:

```
42

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In [8], line 3
      1 with TemporaryVariables(locals(), x=42):
      2     print(x)
----> 3 print(x)

NameError: name 'x' is not defined
```

Finally, notice the difference between local and global scoping:


```python
def f():
    print('inside f with b =', b)


def scope_test():
    with TemporaryVariables(globals(), b=2) as q:
        f()

    with TemporaryVariables(locals(), b=2) as q:
        f()

scope_test()
```

Now, only the variable `b` that is defined in the global scope can be used in
functions called from within the `with`:

```
inside f, with b = 2

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

Cell In [9], line 13
     10     with TemporaryVariables(locals(), b=2) as q:
     11         f()
---> 13 scope_test()


Cell In [9], line 11, in scope_test()
      7     f()
     10 with TemporaryVariables(locals(), b=2) as q:
---> 11     f()


Cell In [9], line 2, in f()
      1 def f():
----> 2     print('inside f, with b =', b)


NameError: name 'b' is not defined
```


Happy hacking!
