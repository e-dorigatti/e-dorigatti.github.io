---
layout: post
title: "How to save locally the result of XPath queries in Firefox and Chrome"
date: 2023-08-11 12:00:00 +0200
categories:
 - Development
---

It happens relatively often that, while browsing the internet like a normal person, I want to extract some data from a webpage, save it locally, and manipulate it in some way.
Since it is an one-off operation, I really do not want to bother writing a web-scraper with Python.
Instead, here is a simple way of doing this through the developer console in Firefox or Chrome!

<!-- more -->

Simple scraping tasks can often be achieved by navigating to a page and executing some [Xpath][xp] queries to extract the elements of interest.
Python and Selenium can be used to write complex web-scrapers to automate this kind of web navigation and data gathering, but this way is too cumbersome for small, one-off scraping tasks.
I have been looking for a way of doing this directly in the developer console of my browser as I navigate to the page I am interested in, but while executing Xpath is trivial via `$x('//some/path')`, saving the results is not.

## The trick

Until, at last, I found [this solution on StackOverflow][so], allowing one to save objects as JSON directly from the console:

```javascript
function downloadObjectAsJson(exportObj, exportName){
  var dataStr = "data:text/json;charset=utf-8," +
    encodeURIComponent(JSON.stringify(exportObj));
  var downloadAnchorNode = document.createElement('a');
  downloadAnchorNode.setAttribute("href",     dataStr);
  downloadAnchorNode.setAttribute("download", exportName + ".json");
  document.body.appendChild(downloadAnchorNode); // required for firefox
  downloadAnchorNode.click();
  downloadAnchorNode.remove();
}
```

Essentially, this snippet:

 1. Serializes the object to be saved into JSON,
 1. Adds to the page a temporary `a` element whose `href` attribute is set to the encoded data to be saved,
 1. Simulates a click from the user, tricking the browser into downloading the data to a file,
 1. Finally removes this element from the page.

Xpath queries executed via `$x` return arrays of HTML elements, which are not JSON-serializable.
Converting them to an appropriate representation is however very easy:

```javascript
function convertElementArrayToStringArray(element_array) {
  converted = [];

  for(var i = 0; i < element_array.length; i++) {
    if("outerHTML" in element_array[i]) {
      converted.push(element_array[i].outerHTML);
    }
    else {
      converted.push(element_array[i].nodeValue);
    }
  }

  return conv;
}
```

This function converts HTML nodes to their `outerHTML` representation, while keeping text nodes as they are.

Executing the query and saving the result is then just a matter of chaining these two functions:

```javascript
function saveSelectorQuery(result) {
  var conv = convertElementArrayToStringArray(result);
  downloadObjectAsJson(conv, "selector-query");
}
```

## Usage

For ease of use, here are the previous functions as a single snippet:

```javascript
function downloadObjectAsJson(exportObj, exportName){
  var dataStr = "data:text/json;charset=utf-8," +
    encodeURIComponent(JSON.stringify(exportObj));
  var downloadAnchorNode = document.createElement('a');
  downloadAnchorNode.setAttribute("href",     dataStr);
  downloadAnchorNode.setAttribute("download", exportName + ".json");
  document.body.appendChild(downloadAnchorNode); // required for firefox
  downloadAnchorNode.click();
  downloadAnchorNode.remove();
}

function convertElementArrayToStringArray(element_array) {
  converted = [];

  for(var i = 0; i < element_array.length; i++) {
    if("outerHTML" in element_array[i]) {
      converted.push(element_array[i].outerHTML);
    }
    else {
      converted.push(element_array[i].nodeValue);
    }
  }

  return converted;
}

function saveSelectorQuery(result) {
  var conv = convertElementArrayToStringArray(result);
  downloadObjectAsJson(conv, "selector-query");
}
```

Simply copy-paste these into the developer console, then call the last function with your selector to download the results!

For example, executing `saveSelectorQuery($x("//h2"))` on this very web page (try it!) will download a file called `selector-query.json` with the following contents:
```
["<h2 id=\"the-trick\">The trick</h2>","<h2 id=\"usage\">Usage</h2>","<h2 class=\"footer-heading\">Emilio's Blog</h2>"]
```
which are exactly the second-level headers in the post.
To only get the titles of the headers, without the surrounding HTML, simply append '/text()' at the end of the previous query.

After this, read the JSON file with your favorite programming language and have fun!


[xp]: https://en.wikipedia.org/wiki/XPath
[so]: https://stackoverflow.com/a/30800715
