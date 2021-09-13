# Flow of Control with Python #

---

__Control flow__

The order in which the individual python statement, expression and function call are evaluated. Explicit control flow is a feature of imperative progamming languages, like Python, in contrast to declarative programming languages (e.g., SQL). A control statement in Python enable the program to _make a decision_ and follow one execution path instead of another. Control flow ensures that your Python program can follow multiple paths (bifurcate, repeat, bypass), instead of just a linear execution.

---

## Branching with Boolean Values ##

* Boolean errors

```py
>>> spock = True
>>> spock
True
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>>
>>> True = 2+2
  File "<stdin>", line 1
SyntaxError: can't assign to keyword
```

| Operator | Meaning |
| - | - |
| `==` | equal to|
| `!=` | not equal to|
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

* Boolean integer tests

```py
>>> 23 == 23
True
>>> 23 == 5
False
>>> 2 != 3
True
>>> 5 != 5
False
```

* String and float tests

```py
>>> 'spock' == 'spock'
True
>>> 'spock' == 'Spock'
False
>>> 'spock' != 'kirk'
True
>>> False == False
True
>>> 23.0 == 23
True
>>> 23 == '23'
```

* leg/geq

```py
>>> 5 < 23
True
>>> 5 > 23
False
>>> 23 < 23
False
>>> spock = 25
>>> spock <= 25
True
>>> kirk = 24
>>> kirk >= 10
True
```

variable assignment vs. equality test

* `==` operator compares two values
* `=` operator assigns a value to a variable

### Boolean operators ###

Boolean operators (NOT/AND/OR) compare Boolean values/expressions (True/False).

Negation, NOT/$\lnot$

| Expression | not `True` | not `False` |
| - | :-: | :-: |
| Evaluates to...  | __F__ | __T__ |

```py
>>> A = True
>>> not A
False
>>> B = False
>>> not B
True
>>> not not B
False
```

Conjunction, AND/$\land$

| Expression | `True` and `True` | `True` and `False` | `False` and `True` | `False` and `False` |
| - | :-: | :-: | :-: | :-: |
| Evaluates to...  | __T__ | __F__ | __F__ | __F__ |

```py
>>> A = True
>>> A and A
True
>>> B = False
>>> A and B
False
>>> B and A
False
>>> B and B
False
```

Disjunction, OR/$\lor$

| Expression | `True` or `True` | `True` or `False` | `False` or `True` | `False` or `False` |
| - | :-: | :-: | :-: | :-: |
| Evaluates to...  | __T__ | __T__ | __T__ | __F__ |

```py
>>> A = True
>>> A or A
True
>>> B = False
>>> A or B
True
>>> B or A
True
>>> B or B
False
```


#### Mixing Boolean and Comparison Operators ####

```py
>>> (0 < 1) and (1 < 2)
True
>>> (0 < 1) and (2 < 1)
False
>>> (0 == 1) or (1 == 1)
True
>>> ()
```

#### Examples ####

What is the largest number?

```py
x = 1
y = 3
z = 2
if (x > y) and (x > z):
    print("x is larger than y and z")
elif (y > x) and (y > z):
    print("y is larger than x and z")
else:
    print("z is larger than x and y")
```

implement XOR (exclusive OR)

```py
>>> x = 1
>>> y = 2
>>> (x == x or y != y) and not (x == x and y != y)
True
>>> (x == x or y == y) and not (x == x and y == y)
False
```

### Elements of Flow Control ###

* condition is an expression `x > y` in the context of flow control
* blocks of code are groups of python lines
  * a block begins with an indentation (PEP8: use four spaces instead of tab)
  * blocks can be embedded in other blocks
  * a block end with ińdentation decrease (four spaces/tab pr block)

```py

name = 'Kathryn'
password = 'voyager'

if name == 'Kathryn':
    print(f'Hello, {name}')
    if password == 'voyager':
        print('Please enter')
    else:
        print('Error, please try again')
```

* this is an example on program execution that starts with a CASE (`name` test) followed by a SELECTION (`if ... else`) flow where the program bifurcates.

### Flow Control Statements ###

#### `if` statement ####

* SELECTION or CASE control flow (initial statement)

Components

* the `if` keyword
* a condition (evaluates to `True` or `False`)
* a `:`
* `if` clause: next line indented (4 spaces) code block

```py
if name == 'Kathryn':
    print(f'Hello, {name}.')
```

#### `else` statement ####

* SELECTION control flow

Components

* the `else` keyword
* a `:`
* `else` clause: next line indented (4 spaces) code block

```py
if name == 'Kathryn':
    print(f'Hello, {name}.')
else:
    print('Hello, who are you?')
```

#### `elif` statement ####

CASE flow control

Components

* `elif` keyword
* a condition (evaluates to `True` or `False`)
* a `:`
* `elif` clause: next line indented (4 spaces) code block

```py
if name == 'Kathryn':
    print(f'Hello, {name}.')
elif name == 'Seven of Nine':
    print(f'Hello, {name}, Tertiary Adjunct of Unimatrix Zero O')
```

* add additional CASEs

```py
if name == 'Kathryn':
    print(f'Hello, {name}.')
elif name == 'Seven of Nine':
    print(f'Hello, {name}, Tertiary Adjunct of Unimatrix Zero O')
elif name == 'Kirk':
    print('You don't belong here')
```

* close with a SELECTION

```py
if name == 'Kathryn':
    print(f'Hello, {name}.')
elif name == 'Seven of Nine':
    print(f'Hello, {name}, Tertiary Adjunct of Unimatrix Zero O')
elif name == 'Kirk':
    print('You don't belong here')
else:
    print('Hello, who are you?')
```

#### `while` loop statement ####

Components

* the `while` keyword
* a condition (evaluates to `True` or `False`)
* a `:`
* `while` clause: next line indented (4 spaces) code block

Compare `if` to `while`

```py
>>> if var < 5:
...     print('foobar')
...     var = var + 1
...
foobar
```

```py
>>> var = 0
>>> while var < 5:
...     print('foobar')
...     var = var + 1
...
foobar
foobar
foobar
foobar
foobar
```

make script and try (annoying) while loop

```py
name = ''
while name != 'exit':
    print('Enter your name')
    name = input()
    if name != 'exit':
        print(f'well hello {name}')
print('Thank you')
```

* caught in infinite loop

```py
while True:
    print('in the loop...')
```

* exit with `Ctrl + c` or `CMD + c`


#### `break` statement ####

* use onside loop

```py
while True:
    print('Enter your name')
    name = input()
    if name == 'exit':
        break
    print(f'well hello {name}')
print('Thank you')
```

#### `continue` statement ####

* use onside loop

```py
while True:
    print('Your name please:')
    name = input()
    if name != 'Spock':
        continue
    print(f'Hello {name}. What is the password? (It is borg)')
    password = input()
    if password == 'borg':
        print(f'Ok {name}, you are in the clear')
        break
```

#### Truety or Falsey values ####

```py
>>> 0 == False
True
>>>  0.0 == False
True
```

```py
>>> test = ''
>>> if test:
        print('test successful')
>>> test = 'something'
>>> if test:
        print('test successful')
test successful
```

#### `for` loops and `range()` ####

Components

* the `for` keyword
* a (loop) variable name
* the `in` keyword
* a call to the `range()` function with up to three parameters (integers)
* a `:`
* `for` clause: next line indented (4 spaces) code block

```py
>>> print('How are you')
>>> for i in range(5):
...     print(f'good * {i}')
good * 0
good * 1
good * 2
good * 3
good * 4
```

NB: remember that `break` and `continue` statements can be used inside loops

* summing consecutive values

```py
total_sum = 0
for num in range(101):
    total_sum = total_sum + num
print(total_sum)

5050
```

* implement consecutive sum with `while` statement

```py
total_sum = 0
num = 0
while num < 101:
    total_sum = total_sum + num
    num = num + 1 
print(total_sum)
```

##### Parameters of `range()` #####

* `range()` is inclusive in the beginning, but exclusive in the end

```py
for i in range(12, 18, 2):
    print(i)
12
14
16
```

* backwards

```py
for i in range(3, -1, -1):
    print(i)
3
2
1
0
```

