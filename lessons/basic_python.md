
* entering command in the interacitve shell/Read-Evaluate-Print Loop
* REPL allows line-by-line execution

## Entering an expression

* basic math operations

```py
>>> 2 + 2
4
>>> 2 ** 3
8
>>> 22 % 8
6
>>> 22 // 8 # integer division/floored quotient
2
>>> 22 / 8
2.75
>>> 3 * 5
15
>>> 5 - 2
3
```

### Precedence

* order of operations
* order of operations (**, %, //, /, *, -, +)

```py
>>> 2 + 3 * 6
20
>>> (2 + 3) * 6
30
>>> (5 - 1) * ((7 + 1) / (3 - 1))
16.0
```

### Error

* `SyntaxError` error message
* The most common reason of an error in a Python program is when a certain statement is not in accordance with the prescribed usage. Such an error is called a syntax error. The Python interpreter immediately reports it, usually along with the reason.


```py
>>> print 'hello'
  File "<stdin>", line 1
    print 'hello'
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?
```
* In Python 3.x, print is a built-in function and requires parentheses. The example statement violates this usage and hence syntax error is displayed.


```py
>>> 5 +
  File "<stdin>", line 1
    5 +
      ^
SyntaxError: invalid syntax
```


```py
>>> 2 +* 3
  File "<stdin>", line 1
    2 +* 3
       ^
SyntaxError: invalid syntax
>>> 
```

* breaking down the error message
    * The file name where the invalid syntax was encountered
    * The line number and reproduced line of code where the issue was encountered
    * A caret (^) on the line below the reproduced code, which shows you the point in the code that has a problem
    * The error message that comes after the exception type SyntaxError, which can provide information to help you determine the problem

```sh
File "src/tracebackerror.py", line 11
    2 +* 3
       ^
SyntaxError: invalid syntax
```

#### Type of errors

* Important built-in exceptions in Python.

| Exception | Description |
| -- | -- |
| AssertionError | Raised when the assert statement fails. |
| AttributeError | Raised on the attribute assignment or reference fails. |
| EOFError | Raised when the input() function hits the end-of-file condition. |
| FloatingPointError | Raised when a floating point operation fails. |
| GeneratorExit | Raised when a generator's close() method is called. |
| ImportError | Raised when the imported module is not found. |
| IndexError | Raised when the index of a sequence is out of range. |
| KeyError | Raised when a key is not found in a dictionary. |
| KeyboardInterrupt | Raised when the user hits the interrupt key (Ctrl+c or delete) |.
| MemoryError | Raised when an operation runs out of memory. |
| NameError | Raised when a variable is not found in the local or global scope. |
| NotImplementedError | Raised by abstract methods. |
| OSError | Raised when a system operation causes a system-related error. |
| OverflowError | Raised when the result of an arithmetic operation is too large to be represented. |
| ReferenceError | Raised when a weak reference proxy is used to access a garbage collected referent. |
| RuntimeError | Raised when an error does not fall under any other category. |
| StopIteration | Raised by the next() function to indicate that there is no further item to be returned by the iterator. |
| SyntaxError | Raised by the parser when a syntax error is encountered. |
| IndentationError | Raised when there is an incorrect indentation. |
| TabError | Raised when the indentation consists of inconsistent tabs and spaces. |
| SystemError | Raised when the interpreter detects internal error. |
| SystemExit | Raised by the sys.exit() function. |
| TypeError | Raised when a function or operation is applied to an object of an incorrect type. |
| UnboundLocalError | Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. |
| UnicodeError | Raised when a Unicode-related encoding or decoding error occurs. |
| UnicodeEncodeError | Raised when a Unicode-related error occurs during encoding. |
| UnicodeDecodeError | Raised when a Unicode-related error occurs during decoding. |
| UnicodeTranslateError | Raised when a Unicode-related error occurs during translation. |
| ValueError | Raised when a function gets an argument of correct type but improper value. |
| ZeroDivisionError | Raised when the second operand of a division or module operation is zero. |

* `IndexError`

```py
>>> l = [1, 1, 2, 3, 5]
>>> l[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

* `ModuleNotFoundError`

```py
>>> import notamodule
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'notamodule'
```

* `KeyError`

```py
>>> captains = {'Enterprise' : 'Kirk', ' Voyager' : 'Janeway', 'DS9' : 'Sisko'}
>>> captains['BorgCube']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'BorgCube'
```

* `ImportError`

```py
>>> from math import borgcube
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'borgcube' from 'math' (unknown location)
```

* `NameError`

```py
>>> borg
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'borg' is not defined
```

* `ValueError`

```py
>>> int('borg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'borg
```

### Data types (simple)

| Data Type | Example |
| --- | --- |
| Integer | ... -1, 0, 1 ...|
| Floating-point Number | ... -1.0, 0.0, 1.0 ... |
| String | 'a', 'ab', 'abc' |

#### String manupulation

* `SyntaxError` EOL (end of line), forgot to close the string
```py
>>> 'hello Spock
  File "<stdin>", line 1
    'hello Spock
               ^
SyntaxError: EOL while scanning string literal
```

* Concatenation

```py
>>> 'Kathryn' +  'Janeway'
'KathrynJaneway'
```

* `TypeError` for string concatenation

```py
>>> 'Janeway' + 35
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

* string formatting

```py
>>> 'Janeway %s' % 35
'Janeway 35'

>>> 'Janeway {}'.format(35)

>>> f'Janeway {35}'
'Janeway 35'
```

* f-strings: 'formatted string literals,' f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values. The expressions are evaluated at runtime and then formatted using the `__format__` protocol.

```
>>> 'Kathryn'*5
'KathrynKathrynKathrynKathrynKathryn'

>>> 'Kathryn'*'Spock'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'

>>> 'Kathryn'*5.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
```

## Variable assignment

* variable: a value assigned a label

```py
>>> spock = 50 # initialize variable
>>> spock
50
>>> janeway = 35
>>> spock + janeway 
85
>>> spock + janeway + janeway
135
>>> spock = spock + 5 # assigne new value to variable (old is  overwritten)
>>> spock
55
```

* overwrite string

```py
>>> captain = 'Kirk'
>>> captain
'Kirk'
>>> captain = 'Piccard'
>>> captain
Piccard
```

### Valid variable names

* one word with no spaces
* only use letters, numbers and underscore
* cannot begin with number

| Valid | Invalid |
| --- | --- |
| snake_case | snake-case |
| camelBack | camel back |
| wnumber23 | 23wnumber |
| _23 | 23 |
| TOTAL_SUM | TOTAL_$UM |
| hello | 'hello' |


## Advanced topics

* Linting: Linting highlights syntactical and stylistic problems in your Python source code, which oftentimes helps you identify and correct subtle programming errors or unconventional coding practices that can lead to errors. For example, linting detects use of an uninitialized or undefined variable, calls to undefined functions, missing parentheses, and even more subtle issues such as attempting to redefine built-in types or functions.  Linting is thus distinct from Formatting because linting analyzes how the code runs and detects errors whereas formatting only restructures how code appears. (see `linting.py`)

---

* content
    - snake case for variables, camel case for classes
    - "Consistency with the style guide is important. But most importantly: know when to be inconsistent—sometimes the style guide just doesn’t apply. When in doubt, use your best judgment."
* advanced content
    - mutable and immutable data types
      * mutable: list, dictionary, set, user-defined classes
      * immutable: int, float, decimal, bool, string, tuple, range
    - deep and shallow copy: see `var_copy.py`   