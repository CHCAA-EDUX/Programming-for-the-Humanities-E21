# Exercises for Web Scraping

Before you begin you need to install `requests` and `beautifulsoup4` by running the following in the terminal:

```
pip install requests beautifulsoup4
```

## Pair Programming
For each exercise it is required that you import the modules `requests` and `beautifulsoup4` e.g.
```
import requests
import bs4
```

### Exercise 1
Extract all headlines from https://tv2.dk and print them to the console

### Exercise 2
Extract all names and titles of researchers from https://www.au.dk/om/presse/ekspertlister/corona and 
print them to the console

### Exercise 3
Extract all 46 comic book titles from http://comicscontainer.dk/comicbooks?dynamicSearch=ru&page=1 
and save them to a file (`comic-book-titles.txt`)

**Hint** Consider how you will determine when you have reached the last page (last page + 1), so you don’t get an infinite loop

**Hint** The markup is not very well-structured, so you probably need to make several sub-queries on the initial result from bs4

---

## Check your Understanding
1. What type of object is returned by requests.get()? How can you access
   the downloaded content as a string value?
2. How can you view (in the developer tools) the HTML of a specific element
   on a web page?
3. What is the CSS selector string that would find the element with an id
   attribute of main?
4. What is the CSS selector string that would find the elements with a CSS
   class of highlight?
5. What is the CSS selector string that would find all the `<div>` elements
   inside another `<div>` element?
6. What is the CSS selector string that would find the `<button>` element
   with a value attribute set to favorite?
7. Say you have a Beautiful Soup Tag object stored in the variable spam for
   the element `<div>Hello, world!</div>`. How could you get a string 'Hello,
   world!' from the Tag object?
