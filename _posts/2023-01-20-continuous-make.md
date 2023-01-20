---
layout: post
title: "Automatically triggering make when editing files"
date: 2023-01-10 12:00:00 +0200
categories:
 - Development
---

Shortening the edit-build-test cycle as much as possible can greatly increase
your productivity. This post presents an useful trick to run make, or any other
command, every time a file is modified. I mainly use this when working with
LaTeX to compile a PDF upon save, but I can imagine many other use-cases.

<!-- more -->

Without further ado, here's the command as a `make` rule:

```
.PHONY: watch

# other rules ...

watch:
    while true; do \
        find . -type d -not -path "./.git*" -not -path "./build*" \
            | xargs inotifywait \
                --event move,modify,close_write,moved_to,create,delete \
                --exclude "./.git/\|./build/*" ; \
            make ; \
    done
```

So that invoking `make` alone builds the project, while `make watch` starts this
 continuous edit-build loop. For example, I used this in my [pandoc template for
 beamer][pd] so that I can write slides in Markdown using vim or emacs on the
 left half of the screen and a PDF preview on the right half. Thanks to this
 trick, the PDF preview is updated as soon as I save even faster than Overleaf!

The central part of this command is the `inotifywait` part: this little program
simply waits until a file or folder is created, deleted, or modified in one of
the paths that we specified as argument (more on this in a minute). When this
happens, `inotifywait` just terminates, and at this point the following command,
in this case `make`, is triggered. Finally, all of this is enclosed into a
`while true` loop to repeat forever.

To tell `inotifywait` where to watch for changes we use `find` to look for all
folders in the current path, excluding `.git`, `build` and everything below them
(apparently, [excluding][ex] files from `find` is far from trivial).

This only works on Linux, but a similar version can be written for OS X and
Windows as well using [fswatch][fs] instead of `inotifywait`.



  [fs]: https://stackoverflow.com/a/13807906
  [ex]: https://stackoverflow.com/q/4210042
  [pd]: https://github.com/e-dorigatti/pandoc_beamer_template
