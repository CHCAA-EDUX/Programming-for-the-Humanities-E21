# Functions in Python #

A function is a block of statements (a 'bundle of code') that (should) perform one specific task. Bundling your code as functions modularize your program into smaller chunks. As such functions make your code more organized and easier to re-use.

Create a simple script `hello.py` with one function that takes no input and prints hello (in Klingon)

```py
def hello():
    """
    Print hello in Klingon
    """
    print('nuqneH!')
    print('nuqneH!!!')
    print('Hello there.')

hello()
hello()
hello()
```

* Dependency, install `playsound`

```sh
pip install playsound
```

* say hello


```py
from playsound import playsound
def say_hello():
    """
    Say hello in klingon
    """
    playsound('audio.mp3')

say_hello()
say_hello()
say_hello()
```

* Purpose of a function is to group code in order to re-use it multiple times.
* DRY: _Do not Repeat Yourself_ you should always minimize repetitions, that is, avoid duplicating code. Never use `ctrl+c` or `cmd+c`

## `def` statements with parameters ##

The general form of a function in Python is

```py
def function_name(parameters):
    """docstring"""
    statement(s)
```

A value passed to a function is called an _argument_, e.g., `len(some_list)`. Functions have _parameters_ that you pass arguments to, that is, an argument is stored as a parameter of the function.

```py
def hello(name):
    print(f'Hello {name}')

hello('Spock')
hello('Uhura')
```

Notice that a value stored as a parameter by default only has local score, that is, the variable `name` is forgotten after program execution


```py
def play_file(audiofile):
    """
    Play audio file

    Paramters:
        - audiofile: str, filename (path to)
    """
    playsound(audiofile)

play_file('audio.mp3')
```

### Define, Call, Pass, Argument, Parameter ###

* _define_ a function is when you create it (a function is just a type of object in Python) (function definition)
  * `def` statements define functions
* you _call_ a function when you use is (function call)
* a value passed to a function call is an _argument_ (function external)
* a value is assigned to function as a _parameter_ (function internal)

## Return values and `return` statements ##

most functions have return values when called

* return values are specified with the return statement that uses the `return` keyword followed by the expression to be returned

Make script `comments.py`

```py
import random

def tweet_comment(state): # define function
    if state == 1:
        comment = 'This. Is concerning.'
    elif state == 2:
        comment = 'TAKE NO MORE'
    elif state == 3:
        comment = 'So gosh darn amazing!'
    elif state == 4:
        comment = "Do you think Ninja's sneak up on their family  members just for fun?"

    return comment

i = random.randint(1,4) # create variable to be passed as argument
tweet = tweet_comment(i) # function call, i is assigned to parameter state
print(tweet) # print return value
```

and in a single liner (don't do this)

```py
print(tweet_comment(random.randint(1,4)))
```

## The `None` value ##

The `None` keyword is used to define the null value in Python. It is not an empty string, False, or a zero, but a instance of the `NoneType` object. `None` can be assigned to a variable to reset it/reset it to an empty state.

* all functions need to evaluate to a return value and `None` is used as return value in cases where there is no return

```py
>>> hello = print('Hello!!!')
Hello!!!
>>> None == hello
True
```

Or with your custom functions

```py
>>> def xequals1():
...     x = 1
...
>>> y = xequals1()
>>> None == y
True
```

## Function arguments ##

* function arguments can be identified by _position_ (positional arguments) or _keyword_ (keyword arguments)
* _Positional arguments_ are arguments that can be called by their position in the function definition
* _Keyword arguments_ are arguments that can be called by their name.
* _Required arguments_ are arguments that must passed to the function.
* _Optional arguments_ are argument that can be not passed to the function. In python optional arguments are arguments that have a default value

```py
def additive(x, y, z = 1):          # a & b required, c optional
    return x + y * z

res = additive(1, 2)                # positional and default
res = additive(1, 2, 3)             # positional
res = additive(z = 5, y = 2, x = 2) # named
res = additive(y = 2, x = 2)        # named and default
res = additive(5, z = 2, y = 1)     # positional and named
res = additive(8, y = 0)            # positional, named, and default
```

Example with `print()`

```py
print('Hello', end='') # positional and named
print('World')
>>> print('1', '2', '3')
1 2 3
>>> print('1', '2', '3', sep='o')
1o2o3
```

BUT

```py
>>> print(sep='o','1', '2', '3')
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

## Local and global variable scope ##

* _Local variables_ parameters and variables assigned to a called function has _local scope_ in the function by default. 
* _Global variables_ variables that exists outside functions have a global scope
* one global scope (your program), a local scope is created whenever a function is called. When the function reaches its return statement, its scope stops

Impact of scope

* code in global scope cannot use local variables
* code in local scope can access global variables
* code in a function's local scipe cannot use variables in any other local scope
* the same variable name can be used in different scopes for different variables

```py
def hello(name = None):
    print(f'Hello {name}')# name has local scope

name = 'Kathryn'# global scope
hello(name = name)
```

Python has four scopes, built-in (not in example code), global, enclosing (for embedded functions), and local


```py
x = 'Global Scope'
print(x)

def outer_func():
    x = 'Enclosing scope'
    print(x)

    def inner_func():
        x = 'Local scope'
        print(x)

    inner_func()
    print(x)

outer_func()
print(x)
```

### Local variables are NOT in global scope ###

```py
def hello():
    name = 'Kathryn'
hello()
print(name)
```

will give you a `NameError`, why? Because `name` is only in local scope

### Local variables are only local to one context ###

```py
def hello():
    name = 'Kathryn'
    nuqneH()
    print(name)

def nuqneH():
    name = 'Worf'

hello()
```

### Global variables are in the scope of local variables ###

```py
def hello():
    print(name)

name = 'Kathryn'
hello()
print(name)
```

### local and global variable can have same name ###

```py
def hello():
    name = 'Kathryn'
    print(f'{name} local')     # local scope

def nuqneH():
    name = 'Worf'
    print(f'{name} local')
    hello()
    print(f'{name} local')

name = 'Picard'
nuqneH()
print(f'{name} global')
```

## `global` statment ##

* allows you to modify a global variable locally

```py
def hello():
    global name
    name = 'Kathryn'

name = 'Worf'
hello()
print(name)
```

Four scope rules

1. a variable used in global scope is always a global variable
2. with a global statement in a function, a variable becomes global
3. if a variable is used in an assignment statement in the function, it is a local variable
4. if not used in an assignment statement, it is a global variable 

## Exception handling ##

To avoid that your program crashes due to an error/exception, you need to detact and handle errors - _exception handling_

`zero_divide.py`

```py
def divide_by(denominator):
    return 23 / denominator

print(divide_by(3))
print(divide_by(5))
print(divide_by(0))
print(divide_by(1))
```

```sh
7.666666666666667
4.6
Traceback (most recent call last):
  File "script.py", line 6, in <module>
    print(divide_by(0))
  File "script.py", line 2, in divide_by
    return 23 / denominator
ZeroDivisionError: division by zero
```

Dividing by zeros results in a program-breaking error

Use `try-except` clauses to catch exceptions

```py
def divide_by(denominator):
    try:
     return 23 / denominator
    except ZeroDivisionError:
        print('[ERROR] Invalid Argument... ')

print(divide_by(3))
print(divide_by(5))
print(divide_by(0))
print(divide_by(1))
```

```sh
7.666666666666667
4.6
[ERROR] Invalid Argument...
None
23.0
```

