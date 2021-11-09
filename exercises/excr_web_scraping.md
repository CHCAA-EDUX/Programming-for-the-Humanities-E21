# Exercises for Web Scraping

Before you begin you need to install `requests` and `beautifulsoup4` by running the following in the terminal:

```
pip install requests beautifulsoup4
```

## Pair Programming
For each exercise it is required that you import the modules `requests` and `beautifulsoup4` e.g.
```python
import requests
import bs4
```

### Exercise 1
Extract all headlines from https://tv2.dk and print them to the console

**Possible solution** 
```python
import requests
import bs4


def scrape():
    response = requests.get("https://tv2.dk")
    response.encoding = response.apparent_encoding
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    for h2 in soup.select('.tc_heading'):
        print(h2.text)
        

if __name__ == "__main__":
    scrape()
```

### Exercise 2
Extract all names and titles of researchers from https://www.au.dk/om/presse/ekspertlister/corona and 
print them to the console

**Possible solution** 
```python
import requests
import bs4


def scrape():
    page = 1
    count = 0

    response = requests.get("https://www.au.dk/om/presse/ekspertlister/corona")
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    persons = soup.select('.pure-simple-person-single')

    for person in persons:
        name = person.select('.given-name')[0].text + ' ' + person.select('.family-name')[0].text
        title = person.select('.title')[0].text
        print(name, title)


if __name__ == "__main__":
    scrape()
```

### Exercise 3
Extract all 46 comic book titles from http://comicscontainer.dk/comicbooks?dynamicSearch=ru&page=1 
and save them to a file (`comic-book-titles.txt`)

**Hint** Consider how you will determine when you have reached the last page (last page + 1), so you don’t get an infinite loop

**Hint** The markup is not very well-structured, so you probably need to make several sub-queries on the initial result from bs4


**Possible solution** 
```python
import requests
import bs4


def scrape():
    page = 1
    while True:
        response = requests.get("http://comicscontainer.dk/comicbooks?dynamicSearch=ru&page=" + str(page))
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        rows = soup.select('#comicBooks tr')
        if len(rows) == 0:
            break
        for row in rows[1:]:
            print(row.select('td a')[1].text)
        page += 1


if __name__ == "__main__":
    scrape()
```

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
