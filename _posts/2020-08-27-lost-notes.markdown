---
title: "How I almost lost one year worth of notes!"
layout: post
date: 2020-08-27 12:00:00 +0200
markdown: kramdown
categories: PhD
---

<style type="text/css">
table { table-layout: auto; width: 1%; margin: auto; margin-bottom: 15px; }
table td { border-width: 0px; }
table td:nth-child(1) { border-right: 1px solid #e8e8e8; }
table td:last-child { border-left: 1px solid #e8e8e8; }
table tr:nth-child(1) { border-bottom: 1px solid #e8e8e8; }
table tr:last-child { border-top: 1px solid #e8e8e8; }
table tr:nth-child(n) { background-color: white; }
table tr:nth-child(1) { background-color: #f7f7f7; font-weight: bold }
table tr td:nth-child(1) { background-color: #f7f7f7; font-weight: bold }
</style>

I accidentally deleted most newline characters in my 10-thousands-lines,
65-thousands-words notes, painstakingly collected during over a year of PhD!
This is how I recovered them.

<!-- more -->

In my defense, deleting newlines in Vim is easier than it sounds: use `J` in
normal mode to join the line containing the cursor and the next one, or in
visual mode to merge all highlighted lines into one. Now, I use emacs in evil
mode to keep my notes in a huge org-mode file, which is not too different from
markdown. Emacs can collapse sections into a single line showing only the
header, and using `J` on the collapsed header removes all newlines in the whole
section! I must have unintentionally done it on a top-level header, and in a
hurry I must have saved and quit emacs without realizing the damage.

I found about this nice surprise only on the next day. I honestly did not know
this command even existed, so you can imagine my confusion when I saw everything
collapsed into one line! The most recent backup I had was eleven days old;
although I keep the notes in a git repository, I frequently forget to commit new
changes (ahem...).

After a few minutes of desperation spent hopelessly inserting newlines by hand,
I realized I had to find another way. Most newlines occur in predictable places,
so I could write a few rules that would allow me to restore most of them.

No, too complicated and probably not very effective.

Perhaps I could use the old backup to find where to insert newlines, keeping
cursors on the two files, sliding forward and comparing characters on the way.
But I also added content. I could look ahead on the new file whenever I find a
difference, hoping to catch whatever was on the old file after I passed the part
that was added. But how to deal with deletions?

## The minimum edit distance
After a few minutes of deliberation, I realized where my train of thoughts was
bringing me: to the [Wagner-Fischer algorithm][wfa], an algorithm used to find
the minimum edit distance (MED) between two strings that I studied years ago at
University. Essentially, given two strings, the problem is to find the minimum
number of character edits (insertions, deletions, and replacements) to transform
one string into the other.

For example, the MED between `bc` and `abc` is one: just add `a` at the
beginning. The MED between `abc` and `acc` is also one, since the middle `b` can
be swapped with a `c`. In general, when the two strings start with the same
character, their MED equals the MED of the remaining part: the MED between `abc`
and `acc` is the same as the MED of `bc` and `cc`.

When the first character is different, we can either replace it, remove it or
insert it at the beginning of the first string, then look at the remainder of
the strings. We need to compute the MED in each case, take the minimum, and add
one (for the edit at the first character). Consider `MED(bc, abc)`, we can
either:

 - Replace the first character: `MED(bc, abc) = 1 + MED(ac, abc)`; or
 - Insert an `a` at the beginning of the first string: `MED(bc, abc) = 1 +
   MED(abc, abc)`; or
 - Remove the `b` at the beginning of the first string: `MED(bc, abc) = 1 +
   MED(c, abc)`.

Furthermore, in the first two cases we can immediately apply the rule for equal
first characters. This means that we have three choices, all of which involve
a recursive call skipping the first character of one or both strings:

 - Replacement: skip from both strings.
 - Insertion: skip from the first string.
 - Deletion: skip from the second string.

This procedure can be easily transcribed into a recursive algorithm using
memoization to avoid re-computing intermediate results, a simple measure that
reduces the complexity from exponential to quadratic:

```python
def minimum_edit_distance(r, s):
    res = {}

    def recur(i, j):
        # minimum edit distance between r[i:] and s[j:]

        if (i, j) not in res:
            # first time: compute result

            if i >= len(r):
                # base-case: r[i:] is empty, add len(s[j:]) characters
                res[i, j] = len(s) - j
            elif j >= len(s):
                # base-case: s[j:] is empty, add len(r[i:]) characters
                res[i, j] = len(r) - i
            elif r[i] == s[j]:
                # same character: skip
                res[i, j] = recur(i + 1, j + 1)
            else:
                # different character: find best edit
                an = recur(i + 1, j)
                am = recur(i, j + 1)
                ao = recur(i + 1, j + 1)

                if ao < an and ao < am:
                    res[i, j] = ao + 1
                elif an < am:
                    res[i, j] = an + 1
                else:
                    res[i, j] = am + 1

        # return cached result
        return res[i, j]

    return recur(0, 0), res
```


## Recovering the edits

Great, now we know the MED, but how do we get the actual edits? There is no
straightforward way to do this in the previous function. Even though we know
what is the best edit from that point on, we still don't know if we ourselves
are in the best choice or in a sub-optimal branch. There could be a wrong edit
before us, and we would have no way of knowing. We could use lists to store the
optimal choices for each branch and return the appropriate list with our added
edit, but that would be quite ugly and, most importantly, very inefficient.

As you can see from the algorithm above, we are saving the MED for (almost) all
pairs of indices `i` and `j` to avoid re-computation. As it turns out, we can
also use this information to recover the sequence of edits. Suppose that
`r='bc'` and `s='abc'`, then you can think of the algorithm as filling a table
that looks like this:

<table>
  <tbody>
    <tr><td>&nbsp;</td><td>a</td><td>b</td><td>c</td><td>-</td></tr>
    <tr><td>b</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
    <tr><td>c</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
    <tr><td>-</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
  </tbody>
</table>

Where the cell at row `i` and column `j` contains the MED between `r[i:]` and
`s[j:]`. The first cells to be filled are those in the last row and column,
corresponding to the base case where one of the strings is empty:

|   | a | b | c | - |
| b |   |   |   | 2 |
| c |   |   |   | 1 |
| - | 3 | 2 | 1 | 0 |

We now proceed backward, filling the cell corresponding to `r[1:]='c'` and
`s[2:]='c'`. Since the characters are the same, we can copy the value in cell
`(2, 3)`:

|   | a | b | c | - |
| b |   |   |   | 2 |
| c |   |   | 0 | 1 |
| - | 3 | 2 | 1 | 0 |


We can now fill the second row and the third column proceeding again backward.
For each cell, if the characters are the same, use the same value as the cell
below to the right. Otherwise, find the minimum between the cell below, to the
right, and below to the right, and add one to it. Sounds familiar?


|   | a | b | c | - |
| b |   |   | 1 | 2 |
| c | 2 | 1 | 0 | 1 |
| - | 3 | 2 | 1 | 0 |

And go on like this, until the whole table is filled:

|   | a | b | c | - |
| b | 1 | 0 | 1 | 2 |
| c | 2 | 1 | 0 | 1 |
| - | 3 | 2 | 1 | 0 |

The top left cell contains the MED for the two strings.

This iterative procedure I just showed is an alternative way of implementing
dynamic programming algorithms that does not use recursion, but I am not very
fond of it. I find recursion more natural and easier to implement.

Now, the necessary edits can be recovered from the table by finding the path
from the top left to the bottom right cell that has the smallest numbers, while
moving only right, down or both:

|   |                                                 a |                                                 b |                                                 c |                                                 - |
| b | <span style="color:red;font-weight:bold">1</span> | <span style="color:red;font-weight:bold">0</span> |                                                 1 |                                                 2 |
| c |                                                 2 |                                                 1 | <span style="color:red;font-weight:bold">0</span> |                                                 1 |
| - |                                                 3 |                                                 2 |                                                 1 | <span style="color:red;font-weight:bold">0</span> |

Where moving to the right is an insertion, moving down is a deletion, and moving
diagonally is a replacement.

```python
def reconstruct(r, s, d):
    """
    Reconstructs r by applying edits to s accoding to the distance matrix d
    """

    res = []
    i = j = 0
    while i < len(r) and j < len(s):

        # find cost of edits
        an = d.get((i + 1, j), float('inf'))
        am = d.get((i, j + 1), float('inf'))
        ao = d.get((i + 1, j + 1), float('inf'))

        if ao <= am and ao <= an:
            # either same character or replacement, take from new string
            res.append(r[i])
            i += 1
            j += 1
        elif am <= ao and am <= an:
            # character removed from old string, don't insert
            j += 1
        else:
            # insertion from new string, keep modification
            res.append(r[i])
            i += 1

    # read remaining part from new string
    res.extend(r[i:])

    return res
```


This function is not very useful right now, as its result of equals `r`.

We are now going to modify these two functions so that newlines from the backup
are inserted in the right place in the mingled notes, while preserving the other
edits I made.

## Modifications to restore newlines
Modifying the algorithm to restore newlines is actually quite straightforward.
Currently, an unmatched newline from the backup is discarded. We first need to
modify the MED computation so that the newline is always inserted, corresponding
to a skip in the backup.

If the mingled notes contain a corresponding newline, we skip that too.
Technically we would not need to check for this condition, as it will be handled
automatically by the algorithm. However, it would introduce unnecessary
overhead, as the algorithm would need to perform two more recursive calls in the
following step to figure out that the newline in the mingled notes can be
skipped.

```python
def minimum_edit_distance(r, s):
    res = {}

    def recur(i, j):
        # minimum edit distance between r[i:] and s[j:]

        if (i, j) not in res:
            # first time: compute result

            if i >= len(r):
                # base-case: r[i:] is empty, add len(s[j:]) characters
                res[i, j] = len(s) - j
            elif j >= len(s):
                # base-case: s[j:] is empty, add len(r[i:]) characters
                res[i, j] = len(r) - i
            elif s[j] == '\n':
                # *** NEW CASE ***
                # force newline insertion from the old notes
                # skip corresponding newline from mingled notes if present
                if r[i] == '\n':
                    res[i, j] = recur(i + 1, j + 1) + 1
                else:
                    res[i, j] = recur(i, j + 1) + 1
            elif r[i] == s[j]:
                # same character: skip
                res[i, j] = recur(i + 1, j + 1)
            else:
                # different character: find best edit
                an = recur(i + 1, j)
                am = recur(i, j + 1)
                ao = recur(i + 1, j + 1)

                if ao < an and ao < am:
                    res[i, j] = ao + 1
                elif an < am:
                    res[i, j] = an + 1
                else:
                    res[i, j] = am + 1

        # return cached result
        return res[i, j]

    return recur(0, 0), res
```

We also need to mirror this behavior in the reconstruction function: if a
newline is found in the backup, always insert it. The old behavior was to skip
it, since the minimum distance would be obtained with a deletion.

```python
def reconstruct(r, s, d):
    res = []
    i = j = 0
    while i < len(r) and j < len(s):

        # find cost of edits
        an = d.get((i + 1, j), float('inf'))
        am = d.get((i, j + 1), float('inf'))
        ao = d.get((i + 1, j + 1), float('inf'))

        if s[j] == '\n':
            # *** NEW CASE ***
            # force insertion of newlines from backup
            res.append(s[j])
            j += 1

            # skip a possible corresponding newline in the mingdled notes
            if r[i] == '\n':
                i += 1
        elif ao <= am and ao <= an:
            # either same character or replacement, take from mingled notes
            res.append(r[i])
            i += 1
            j += 1
        elif am <= ao and am <= an:
            # character removed from backup, don't insert
            j += 1
        else:
            # insertion from mingled notes, keep modification
            res.append(r[i])
            i += 1

    # read remaining part from mingled notes
    res.extend(r[i:])

    return res
```


## Practicalities

This algorithm works well for short strings, but my notes count around half a
million characters. Even for strings of medium length, this fails with a
`RecursionError`, which occurs when the maximum number of nested function calls
has been reached. This limit is so high (3000 calls on my system) that it is
usually met only with recursive algorithms like this one. Fortunately, it can be
increased easily (thank you [StackOverflow](https://stackoverflow.com/a/16248113)):

```python
import resource
import sys

resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)
```

After increasing the recursion limit, the problem is... Not enough RAM. The
table shown above would have 250 billion cells, needing about 931 GB of memory.
How to deal with this? Well, why use characters? The algorithm works, without
modifications, using words instead of characters. We just need to be careful and
preserve newlines, since that is the reason why we are doing all this. The notes
had about 100,000 words, needing 36 GB of memory. I did not have enough on my
laptop, but I happened to have exclusive access to a machine with 96 GB of RAM,
so I quickly uploaded code and data, ran the script and waited.

And waited.

And waited.

And waited...

Since I could not work without my notes (which also contain agenda, meetings,
todo list, and everything else), I started thinking at another way to speed this
up. I spent some time toying with the idea of splitting the distance matrix in
blocks, and computing the blocks in the same order you compute the cells. I am
sure that would have worked, but as I grew more impatient I started looking for
another way.

Then I had an idea: even though a few things were different, the overall
structure of the document was the same. They had the same top-level headers, and
probably the same level-two headers too. Headers would function as barriers, and
the algorithm could be run separately on the contents of the same header! The
largest section had about 7,000 words, requiring a meager 200 MB to store the
matrix: easily doable on a laptop. I simply had to scan the files, look for the
beginning of level-two headers and match their position. Unmatched sections were
simply merged with the closest previously matched one.

## Pitfalls
The reconstruction was not perfect. For example, deleted newlines in regions
that were not in the backup could not, for obvious reasons, be restored.
Similarly, newlines in regions that were deleted from the backup were preserved,
since we forced this choice. Moreover, most of the indentation was gone, deleted
by `J` together with the newlines (at the time I thought it was a bug in the
algorithm, and I could not figure out the reason or the proper way to deal with
it).

Luckily, `git diff` has options to ignore white space changes, so I could easily
check other unintended consequences of the algorithm. Not much damage was done,
or, I should say, most of the mess was dealt with appropriately by the
algorithm. After fixing a few things by hand and creating a copy of the old,
mingled notes, I committed the fixes.

And the script big machine? Still running.

It was a fun Monday morning.


 [wfa]: https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
