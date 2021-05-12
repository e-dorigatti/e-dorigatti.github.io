---
layout: post
title:  "Embedding files into Jupyter notebooks with clickable download links"
date:   2021-05-12 12:00:00 +0200
categories: Python
---

Sharing Jupyter notebook or exporting them to HTML is a great way of sharing the results of an analysis with other stakeholders. Some analyses however produce additional data that cannot be simply shown in the nobeook. In such cases, your only option is to send additional files along with the notebook. Or is it?

<!-- more -->

## Show me the code!

Imagine you have the following data frame:


```python
import pandas as pd

df = pd.DataFrame({
    'i': [1, 2, 3],
    '2i': [2, 4, 6],
    'ii': [1, 4, 9]
})
```

Here is how to create a download link for it:


```python
from IPython.core.display import display, HTML
from base64 import b64encode

data = b64encode(df.to_csv().encode('utf8')).decode('utf8')
link = f'''
<a href="data:text/csv;base64,{data}"
       download="dataframe.csv">
   Download dataframe
</a>
'''
display(HTML(link))
```



<a href="data:text/csv;base64,LGksMmksaWkKMCwxLDIsMQoxLDIsNCw0CjIsMyw2LDkK"
       download="dataframe.csv">
   Download dataframe
</a>



Try it, the link really works!

The data will be available both in a HTML export and in a Jupyter notebook, even if you restart the kernel. Great for sharing! Try to download the notebook in which I wrote this blog post, [here](/attachments/notebook_embedded_attachment.ipynb).

## How does it work?

It makes use of a [data URI][datauri] together with Jupyter's ability to show arbitrary HTML as the output of a cell. Data URIs allow you to embed arbitrary data in a web page, which is then treated as an external resource (i.e. it can be downloaded). In the snippet above, the data URI is the part inside the `href` attribute of the `a` tag. The rendered HTML looks like this:

[datauri]: https://en.wikipedia.org/wiki/Data_URI_scheme


```python
print(link)
```

    
    <a href="data:text/csv;base64,LGksMmksaWkKMCwxLDIsMQoxLDIsNCw0CjIsMyw2LDkK"
           download="dataframe.csv">
       Download dataframe
    </a>
    


A data URI has the following format:

```
data:[<media type>][;base64],<data>
```

Where the [media type][mime] specifies what the data represents (a CSV file in the example) and the optional `base64` specification indicates whether the data is encoded in [base 64][b64] or plain text. For CSV files you need to use base64, otherwise the newlines in the file will be ignored (as per the HTML specifications). Finally, The `download` attribute is used to give a name to the CSV file.

Using base64 allows you to embed binary files too; for example, you could compress large data frames or export them as excel files. More advanced use-cases may require using an in-memory buffer, for example:

[b64]: https://en.wikipedia.org/wiki/Base64
[mime]: https://en.wikipedia.org/wiki/Media_type
        


```python
from io import BytesIO

with BytesIO() as buf:
    np.save(buf, df)
    buf.seek(0)
    
    data = b64encode(buf.read()).decode('utf8')
    link = f'''
    <a href="data:application/octet-stream;base64,{data}"
           download="data.npy">
       Download data
    </a>
    '''
    display(HTML(link))
```



<a href="data:application/octet-stream;base64,k05VTVBZAQB2AHsnZGVzY3InOiAnPGk4JywgJ2ZvcnRyYW5fb3JkZXInOiBUcnVlLCAnc2hhcGUnOiAoMywgMyksIH0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAoBAAAAAAAAAAIAAAAAAAAAAwAAAAAAAAACAAAAAAAAAAQAAAAAAAAABgAAAAAAAAABAAAAAAAAAAQAAAAAAAAACQAAAAAAAAA="
       download="data.npy">
   Download data
</a>



Note the media type, `application/octet-stream`, to denote general binary data. Other types you may find useful are `application/vnd.ms-excel` for Excel files and `application/json` for JSON data.

## What limitations does it have?

The most important limitation is data size, as embedding anything but small files will seriously clog Jupyter and the browser itself. For example, a data frame with 25 columns and 100,000 rows consumes only 19 MB, which grows to 62MB once embedded into base64. After displaying the download link, there is a visible delay in some operations such as opening and the notebook, clicking the link, etc. Grow the data size by five or ten times and the browser becomes unuseable.

So you won't be able to embed Big Data(R) in your notebooks, but this method opens a whole lot of new useful use-cases.
