# The `dict` data type in Python #

The dictionary data type is a mutable collection of values, stored as key-value pairs

```py
>>> book = {'title': 'Neuromancer', 'author': "Gibson, William" , 'genre': 'Science fiction'}
```

Unlike [lists](link-to-list_data.md), dictionaries are unordered

```py
>>> book = {'title': 'Neuromancer', 'author': "Gibson, William" , 'genre': 'Science fiction'}

>>> permuatation = {'genre': 'Science fiction', 'author': "Gibson, William", 'title': 'Neuromancer'}

>>> book == permutation
True
```

But insertion order is remembered since Python 3.7

```py

>>> list(book)
['title', 'author', 'genre']

>>> list(permutation)
['genre', 'author', 'title']
```



Entering and ordering data with dictionaries (building a simple book-author database)

```py
books = {'Neuromancer': 'Gibson, William', 'VALIS': 'Dick, Phillip K.'}

while True:
    print('Enter a book: (black to quit)')
    title = input()
    if title == '':
        break
    
    if title in books:
        print(f'{title} is written by {books[title]}')
    else:
        print(f'We do not have author information for {title}')
        print(f'Please enter the author of {titile}':)
        author = input()
        books[title] = author
        print('Thank you, the book database is now updated.')
```

NB. you still need to save the database to re-use new entries

Multiple assignment with `items()` method

```py
for (title, author) in books.items():
    print(f'{author} is the author of {title}')

Gibson, William is the author of Neuromancer
Dick, Phillip K is the author of VALIS
```


`setdefault()` method to ensure that a key exists

```py
import pprint

text = 'Cyberspace. A consensual hallucination experienced daily by billions of legitimate operators, in every nation.'

counter = dict()
for char in text:
    counter.setdefault(char, 0)
    counter[char] = counter[char] + 1

pprint.pprint(counter)
```

Nested dictionaries

```py
all_books = {
    'Neuromancer':{'author': 'Gibson, William', 'year': 1984 , 'genre': 'Science fiction' },
    'VALIS': {'author': 'Dick, Phillip K.' , 'year': 1981, 'genre': 'Science fiction' },
    'Schrödingers Cat Trilogy': {'author': 'Wilson, Robert A.' , 'year': 1979, 'genre': 'Science fiction' }
    }

```