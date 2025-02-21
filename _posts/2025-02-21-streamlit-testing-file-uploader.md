---
date: 2025-02-21 00:00:00 +0200
title: "Headless testing of Streamlit file upload"
layout: post
categories:
 - Development
---

I really like the idea of testing Streamlit web applications with pytest together with the rest of the codebase.
Unfortunately, the Streamlit testing framework does not offer a direct way of interacting file_uploader components, which can be a deal breaker for many developers, me included.
Luckily, it only takes a bit of fiddling to get this to work.
Let's see how!

<!-- more -->

## The problem

The basic idea of testing Streamlit applications is to simulate user interactions programmatically and verify the application's behavior.
Tests can create an instance of the app that does not require a browser to run, then interact with the page and check that the content is as expected, for example:

```python
at = AppTest.from_file("src/app.py")
at.run()

at.selectbox(key="select_template").select("some_option")
at.run()

assert at.warning[0].value == "Option not available".
```

The `at` object is used to access and manipulate the web application.
Unfortunately, for some reason, interacting with file uploader components is much harder than interacting with other components.
They are accessible from the `at` object, but appear as `UnknownElement`, and do not offer any method to actually upload files.

## The solution

It is possible to simulate file upload in tests by storing them into the session state under the appropriate key.
Without further ado:

```python
from pathlib import Path


class UploadedFile:
    def __init__(self, name: str, content: bytes) -> None:
        self.name = name
        self.content = content
        self.size = len(content)

    @staticmethod
    def from_disk(path: Path) -> "UploadedFile":
        return UploadedFile(path.name, path.read_bytes())

    def read(self) -> bytes:
        return self.content


def test_app():
    # ...

    # find the file uploader in the app
    file_uploader = at.get("file_uploader")[0]

    # store UploadedFile objects in the session state - take care of the key!
    at.session_state[file_uploader.proto.id] = [
        UploadedFile.from_disk("test/resources/test_data.csv"),
    ]
    at.run()

    # ...
```

There is just a small gotcha with this solution: subsequent calls to `at.run()` will not have the uploaded files in the session state, only the first call after setting the session state has them.
Handling this behavior should only require minor changes to your app, however.

## Demo

Here's a full-fledged test case:

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_string("""
import streamlit as st

files = st.file_uploader("Data upload:", accept_multiple_files=True)
if files:
    st.session_state['files'] = files
files = st.session_state.get('files', [])

st.info(f"Uploaded {len(files)} files with total length {sum(f.size for f in files)}")
""")
at.run()

file_uploader = at.get("file_uploader")[0]
at.session_state[file_uploader.proto.id] = [
    UploadedFile("file1.txt", "content of file1".encode()),
    UploadedFile("file2.txt", "content of file2".encode()),
]
at.run()

assert at.info[0].value == "Uploaded 2 files with total length 32"
```

Happy testing!
