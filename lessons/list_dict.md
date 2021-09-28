# Lists and Dictionaries #

  Both lists and dictionaries are used to store collections of data

## Lists ##

To write proper programs, we need data types that can contain multiple values and therefore handle large complex data. The `list` data types can store multiple items in a single vairable and is used to store collections of data.

### List data type ###

* a `list` is a value (a list value) that contains multiple values in an _ordered sequence_

```py
>>> captains = ['Kirk', 'Picard', 'Janeway']
>>> date_of_birth = [2233, 2305, 2336]
>>> what_a_mess = ['Q', 11235, False, 3.14]
>>> what_a_mess
['Q', 11235, False, 3.14]
```

#### Indexing lists ####

The list data type is a sequence that allow you to index the individual elements (starting from `0`).

```py
>>> captains = ['Kirk', 'Picard', 'Janeway']
>>> captains[0]
'Kirk'
>>> captains[1]
'Picard'
>>> captains[2]
'Janeway'
>>> print(f'{captains[2]} is my favorite captain')
'Janeway is my favorite captain'
>>> print(f'{captains[0]} is older than {captains[1]} and captains[2]')
```

An index should not exceed the number of values in yhe list (as list index `len(listname) - 1`) and it can _only_ be an integer (type `int`).

```py
>>> captains[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> captains[2.0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not float

>>> captains['2']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not str
```

#### Nested lists ####

Lists can contain nested (other) list values (i.e., a list of lists), which is a convenient data type for managing hierarchical data.

```py
>>> fridge = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]
>>> print(fridge[0])
['pepper', 'zucchini', 'onion']
>>> print(fridge[0][0])
'pepper'
```

#### Negative indices ####

Lists allow you to index from the end (instead of the beginning).

```py
>>> captains = ['Kirk', 'Picard', 'Janeway']
>>> captains[-1]
'Janeway'
```

Negative indexing is actually a shorthand for 

```py
>>> captains[len(captains)-1]
'Janeway'
>>> captains[len(captains)-2]
'Picard'
```

#### Slicing lists ####

Indices can be used to index individual elements (values) and slices (sequences of elements).

```py
>>> captains = ['Kirk', 'Picard', 'Sisko', 'Janeway']
>>> captains[0:4]
['Kirk', 'Picard', 'Sisko', 'Janeway']
>>> captains[1:3]
['Picard', 'Sisko']
>>> xy_only = captains[0:-1]
>>> xy_only
['Kirk', 'Picard', 'Sisko']
>>> captains[:-1]
['Kirk', 'Picard', 'Sisko']
```

#### Chaging values in a list ####

You can assign a value of a list location with an index

``` py
>>> captains = ['Kirk', 'Picard', 'Sisko']
>>> captains[2] = 'Janeway'
>>> captains
['Kirk', 'Picard', 'Janeway']
```

#### List concatenation and replication ####

Like strings (`str`) that is also sequence data, you can use `+` to concatenate lists and `*` for replicate lists.

```py
>>> ['Kirk', 'Picard', 'Janeway'] + [2233, 2305, 2336]
['Kirk', 'Picard', 'Janeway', 2233, 2305, 2336]
>>> [2233, 2305, 2336] * 2
[2233, 2305, 2336, 2233, 2305, 2336]
```

If you are left wondering 'how then do i do element-wise multiplication?' after the last example of replication, then look up `numpy` or use a list comprehension

```py
>>> [item * 2 for item in [2233, 2305, 2336]]
[4466, 4610, 4672]
```

#### Removing elements from a list ####

```py
>>> captains = ['Kirk', 'Picard', 'Sisko', 'Janeway']
>>> del captains[2]
>>> captains
['Kirk', 'Picard', 'Janeway']
```

### Working with lists ###

List allow you to `append()` new elements (just as concatenating from the end)

```py
users = list()
while True:
    print(f'Please enter the name of user {len(users) + 1} or enter nothing to end.')
    name = input()
    if name == '':
        break
    users.append(name)
print('The users are:')
for name in users:
    print(f'   {name}')
```

#### Iterate over lists ####

Because lists are sequence data, you can iterate through evey element in the list with a `for` or `while` statement.

```py
captains = ['Kirk', 'Picard', 'Janeway']
for captain in captains:
    print(captain)
```

```py
i = 0
while i < len(captains):
    print(captains[i])
    i = i + 1
```

---

## Dictionaries ##

The dictionary data type, `dict` is a mutable collection of values, stored as key-value pairs. At a more general level, the dictionary data type represents Python's implementation of hash table. A hash table is a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value.

```py
book = {'title': 'Neuromancer', 'author': "Gibson, William" , 'genre': 'Science fiction'}
```

Unlike [lists](link-to-list_data.md), dictionaries are unordered

```py
book = {'title': 'Neuromancer', 'author': "Gibson, William" , 'genre': 'Science fiction'}

permuatation = {'genre': 'Science fiction', 'author': "Gibson, William", 'title': 'Neuromancer'}

book == permutation
True
```

But insertion order is remembered since Python 3.7

```py

list(book)
['title', 'author', 'genre']

list(permutation)
['genre', 'author', 'title']
```

Notice that because dictionaries are not ordered, they cannot be indexed or sliced as lists. Trying to access an key that does not exist, results in a `KeyError`, which is dictionaries pendent to list's `IndexError`.

```py
>>> book = {'title': 'Neuromancer', 'author': "Gibson, William" , 'genre': 'Science fiction'}
>>> book['summary']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'summary'
```

Entering and ordering data with dictionaries can be extremely powerful, because the dictionaries provide a simple key-based way to access multidimensional data, lets us build a simple book-author database, create `book_author_db.py`

```py
books = {'Neuromancer': 'Gibson, William', 'VALIS': 'Dick, Phillip K.'}

while True:
    print('Enter a book: (blank to quit):')
    title = input()
    if title == '':
        break
    
    if title in books:
        print(f'{title} is written by {books[title]}')
    else:
        print(f'We do not have author information for {title}')
        print(f'Please enter the author of {title}:')
        author = input()
        books[title] = author
        print('Thank you, the book database is now updated.')
```

NB. you still need to save the database to re-use new entries, which we will learn in [lesson 8](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/blob/main/CURRICULUM.md#lesson-8-formats-for-representing-structured-data-csv-and-jsons).

### `keys()`, `values()`, and `items()` Methods ###

`keys()`, `values()`, and `items()` return list-like values for keys, values and both. The return values are not list proper, but they can be used in a loop to iterate over the elements and be transformer into lists with `list()`.

```py
>>> books = {'Neuromancer': 'Gibson, William', 'VALIS': 'Dick, Phillip K.'}
>>> for key in books.keys():
...     print(key)
...
Neuromancer
VALIS
>>> for value in books.values():
...     print(value)
...
Gibson, William
Dick, Phillip K.
```

and `items()` allow multiple assignment in a loop 

```py
>>> for (title, author) in books.items():
...     print(f'{author} is the author of {title}')
...
Gibson, William is the author of Neuromancer
Dick, Phillip K. is the author of VALIS
```

### Check existence of key or value ###

As in lists, we can use the `in` and `not in` operators to test if key or value exits in dictionary.

```py
>>> books = {'Neuromancer': 'Gibson, William', 'VALIS': 'Dick, Phillip K.'}
>>> 'VALIS' in books.keys()
True
>>> 'Wilson, Robert A.' in bools.values()
False
```

### `get()` method ###

The `get()` method allows you to set a default response, with the key is not in the dictionary.

```py
>>> books = {'Neuromancer': 'Gibson, William', 'VALIS': 'Dick, Phillip K.'}
>>> book_query = 'The Wrath of Kahn'
>>> print(f"{book_query} - {books.get(book_query, 'Not available')}")
'Not available'
```

### `setdefault()` method ###

Set default, like `get()` provides a method to set default values in dictionaries. Use the method to ensure that a key exists in a doctionary. Create a word count function in `recommender.py`


```py
import pprint

def wordcounter(text):
  counter = dict()
  for char in text:
    counter.setdefault(char, 0)
    counter[char] = counter[char] + 1
  return counter

text_0 = 'cyberspace a consensual hallucination experienced daily by billions of legitimate operators in every nation'
text_1 = 'the internet is becoming the town square for the global village of tomorrow'

tokens = text_0.split() +  text_1.split()

wordcounts = wordcounter(tokens)
pprint.pprint(wordcounts)
```

#### `pprint()` ####

(from Python documentation) The `pprint()` module provides a capability to 'pretty-print' arbitrary Python data structures in a form which can be used as input to the interpreter. The formatted representation keeps objects on a single line if it can, and breaks them onto multiple lines if they don’t fit within the allowed width.

`pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True)`

Prints the formatted representation of object on stream, followed by a newline. If stream is `None`, `sys.stdout` is used. This may be used in the interactive interpreter instead of the `print()` function for inspecting values (you can even reassign print = pprint.pprint for use within a scope). indent, width, depth, compact and `sort_dicts` will be passed to the `PrettyPrinter` constructor as formatting parameters.

### Nested dictaionaries ###

create a script called `books_db.py`

```py
import pprint

all_books = {
    'Neuromancer':{'author': 'Gibson, William', 'year': 1984 , 'genre': 'Science fiction' },
    'VALIS': {'author': 'Dick, Phillip K.' , 'year': 1981, 'genre': 'Science fiction' },
    'Schrödingers Cat Trilogy': {'author': 'Wilson, Robert A.' , 'year': 1979, 'genre': 'Science fiction' }
    }

```

add  some functionality to query your book collection


```py
def query_books(books, feature):
    for (book, subdict) in books.items():
        print(f'[INFO] {book}/{feature}: {subdict[feature]}')

query_books(all_books, 'year')
```

#### Removing entries ####

Delete a book entry with `del` keyword

```py
del all_books['Neuromancer']
```

Remove individual feature value, but keep feature key

```py
all_books['VALIS']['genre'] = None
```