# String Manipulation with Python #

## Working with Strings

### Single or double quotes?

Valid string assignment
```py
kirk = 'To boldly go where no man has gone before.'
```

Invalid
```py
picard = 'Things are only impossible until they're not.'
```

Valid
```py
spock = "It is the lot of 'man' to strive no matter how content he is."
```

#### Escape characters

Valid
```py
picard = 'Things are only impossible until they\'re not.'

spock = 'It is the lot of \'man\' to strive no matter how content he is.'
```

| Escape character | Result |
| :-: | :-: |
| `\'` | `'`|
| `\"` | `"` |
| `\t` | _Tab_ |
| `\n` | _Newline_ |
| `\\` | `\` |

```py
>>> print("There is a way out of every box, a solution to every puzzle; \n it's just a matter of finding it. \n (Picard)" )
There is a way out of every box, a solution to every puzzle;
it's just a matter of finding it.
(Picard)
```

#### Raw strings
* ignores escape characters
```py
>>> print(r'Things are only impossible until they\'re not.')
Things are only impossible until they\'re not.
```
* useful for Win paths and regular expressions

#### Multiline strings
* escape characters are optional, BUT may impact your IDE
* docstrings use multiline strings


### Indexing and Slicing
* string is sequence data
* zero indexing again

```py
>>> spock = "Highly illogical."
>>> spock[0]
'H'
>>> spock[5]
'y'
>>> spock[-1]
'.'
>>> spock[0:4]
'High'
>>> spock[:4]
'High'
>>> spock[7:]
'illogical.'
```

### `in` and `not in` operators for strings

* as sequence data, `in` and `no in` work similarly to lists

## String concatenation and interpolation

```py
>>> name = 'Janeway'
>>> age = 27
>>> print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')
Hello, my name is Janeway. I am 27 years old
>>> print('Hello, my name is %s. I am %d years old.' % (name, age))
Hello, my name is Janeway. I am 27 years old
>>> print('Hello, my name is {}. I am {} years old'.format(name, age))
Hello, my name is Janeway. I am 27 years old
>>> print(f'Hello, my name is {name}. I am {age} years old')
Hello, my name is Janeway. I am 27 years old
```
* f-string string interpolation is easy to read and manipulate
```py
print(f'Hello, my name is {"Kathryn " + name}. I am {age + 8} years old')
```

## String methods

```
>>> name = 'Janeway'
>>> print(dir(name))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
### Casefolding alphabetic characters

* casefolding with `upper()` and `lower()`
  * return new string/does not modify existing string var
  * `islower()` and `isupper()` for testing the case of the full string

### `ìs<feature>()` methods

| method | True | False |
| --- | --- | --- |
| `isalpha()` | 'janeway' | 'janeway27' |
| `isalnum()` | 'janeway', '27', 'janeway27' | 'janeway!'|
| `isdecimal()` | '27' | 'janeway' |
| `isspace()` | '  ' | 'janeway'|
| `istitle()` | 'Captain Kathryn Janeway' | 'Janeway is captain' |

Input validation
```py
While True:
  print('Select a new password (letters and numbers only):')
  password = input()
  if password.isalnum():
    break
  print('Passwords can only have letters and numbers.')
```

### `startswith()` and `endswith()`

```py
>>> 'Captain Kathryn Janeway'.startswith('Captain')
True
>>> 'Captain Kathryn Janeway'.endswith('way')
True
>>> 'Janeway'.startswith('Janeway') == 'Janeway'.endswith('Janeway')
True
```

### `join()` and `split()`

* tokenization with `split()`
```py
>>> text = 'Hello my name is Captain James Kirk'
>>> text.split()
['Hello', 'my', 'name', 'is', 'Captain', 'James', 'Kirk']
```

* generate string from list of tokens with `join()`
```py
>>> tokens = ['Hello', 'my', 'name', 'is', 'Captain', 'James', 'Kirk']
>>> " ".join(tokens)
'Hello my name is Captain James Kirk'
```

* interpolation with `split()` and `join()`
```py
>>> name = 'Jean-Luc Piccard'
>>> text = 'Hello my name is Captain James Kirk'
>>> f"{' '.join(text.split()[:-2])} {name}"
```

* sentence tokenization with `split()`
```py
>>> mccoy = "Compassion: that's the one things no machine ever had. Maybe it's the one thing that keeps men ahead of them."
>>> mccoy.split('.')
["Compassion: that's the one things no machine ever had", " Maybe it's the one thing that keeps men ahead of them", '']
```

### `partition()`

* pre-post separator, return substrings in tuple, separator inclusive
* partitioning is not recursive/splits on first occurrence only

```py

before, sep, after = 'James T Kirk'.partition('T')
```

### `rjust()`, `ljust()`, `center()`

* padded string with spaces to justify text

```py
>>> name = 'spock'
>>> name.rjust(10)
'     spock'
>>> name_padded_5 = name.rjust(5)
>>> name_padded_10 = name.rjust(10)
>>> (len(name), len(name_padded_5), len(name_padded_10))
(5, 5, 10)
```

```py
>>> '[Validation Start]'.center(50, '=')
```

* usefull for tables

```py
def print_performance(metrics, leftwidth, rightwidth):
  print('Performance'.center(leftwidth + rightwidth, '-'))
    for (metric, score) in metrics.items():
        print(metric.ljust(leftwidth, '.') + str(score).rjust(rightwidth))

performance_metrics = {'precision': 0.75, 'recall': 0.76, 'f1-score': 0.75 , 'support': 254}
print_performance(performance_metrics, 12, 5)
print()
print_performance(performance_metrics, 20, 6)

---Performance---
precision... 0.75
recall...... 0.76
f1-score.... 0.75
support.....  254

-------Performance--------
precision...........  0.75
recall..............  0.76
f1-score............  0.75
support.............   254
```

### `strip()`, `rstrip()`, `lstrip()`

* strip whitespaces (space, tab, newline)

```py
>>> spock = '     Logic is the beginning of wisdom, not the end.     '
>>> spock.strip()
'Logic is the beginning of wisdom, not the end.'
>>> spock.lstrip()
'Logic is the beginning of wisdom, not the end.     '
>>> print('Highly illogical.\n')
Highly illogical.

>>> print('Highly illogical.\n'.rstrip())
Highly illogical.
```

---
**On the safe side**

The control character (sequence of) that indicates newline (aka. End Of Line, Next Line or line break) depend on your operating system (or the operating system used to generate the file, you are processing). Most systems use or combune Carriage Return (CR) and Line Feed. In typewriters change line requires two axes of motion, _down_ and _across_ respectively, but in software these can be combined into one action CR and LF. Unix and Unix-like operating systems only uses LF for newline with the `\n` escape character, while Windows maintain the full CR LF sequence with the escape sequence `\r\n`. When removing trailing newlines from strings in Python `rstrip('\n')` is normally sufficient, but to be on the safe side you can use the `os.linesep` variable:
```
>>> import os
>>> newline_text = 'Highly illogical.\n'
>>> newline_text.rstrip(os.linesep)
'Highly illogical.'
```
---
## Numeric values of characters
* all information is stored as strings of binary numbers (bytes). Every text character can therefore be converted to a number, a so-called _Unicode code point_
```py
>>> for char in "abc": print(ord(char))
97
98
99
>>> for num in [97, 98, 99]: print(chr(num))
a
b
c
>>> ord('a') < ord('b')
True
>>> chr(ord('a') + 1)
'b'
```

More on the relationship between bytes and characters [here](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
