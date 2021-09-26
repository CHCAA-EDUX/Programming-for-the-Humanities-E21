# Exercises: Control Flow #

Solve the following 'Pair programming', 'Check your understanding', and 'Practice questions' challenges in groups of two or four.

## Pair programming ##

Conting vowels:

1. Write a loop that counts the number of vowels in a character string.
2. Test it on a few individual words and full sentences.
3. Once you are done, compare your solution to your neighbor pair's. Did you make the same decisions about how to handle the letter ‘y’ (which some people think is a vowel, and some do not)?

Answer:

```py
vowels = 'aeiouAEIOU'
sentence = 'Mary had a little lamb.'
count = 0
for char in sentence:
    if char in vowels:
        count += 1

print(f'The number of vowels in this string is {count}')
```

## Check your understanding ##

1. How many paths: Consider this code

```py
if 4 > 5:
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')
```

Which of the following would be printed if you were to run this code? Why did you pick this answer?

* A
* B
* C
* B and C

Answer:

* C

2. What Is Truth? 

`True` and `False` booleans are not the only values in Python that are true and false. In fact, any value can be used in an `if` or `elif`. After reading and running the code below, explain what the rule is for which values are considered true and which are considered false.

```py
if '':
    print('empty string is true')
if 'word':
    print('word is true')
if []:
    print('empty list is true')
if [1, 2, 3]:
    print('non-empty list is true')
if 0:
    print('zero is true')
if 1:
    print('one is true')
```

Answer:

a truthy value is a value that is considered true when encountered in a Boolean context, and a falsy (sometimes falsey) is a value that is considered false in a Boolean context

* empty strings are 'falsy' which means they are considered false in a Boolean context, so you can just use `not` string
* non-empty strings are 'truthy' which means they are considered true in a Boolean context
* empty lists are 'falsy' which means they are considered false in a Boolean context, so you can just use `not` list
* non-empty lists are 'truthy' which means they are considered true in a Boolean context
* 0 is 'falsy'
* 1 is 'truthy'

3. That’s Not Not What I Meant:

Sometimes it is useful to check whether some condition is `not` true. The Boolean operator `not` can do this explicitly. After reading and running the code below, write some if statements that use `not` to test the rule that you formulated in the previous challenge.

```py
if not '':
    print('empty string is not true')
if not 'word':
    print('word is not true')
if not not True:
    print('not not True is true')
```

Answer:

```py
if not '':
    print('empty string is falsy')
if not not 'word':
    print('word is true')
if not []:
    print('empty list is falsy')
if [1, 2, 3]:
    print('non-empty list is true')
if not 0:
    print('zero is falsy')
if 1:
    print('one is true')
```


## Practice questions ##

1. What are the two values of the Boolean data type? How do you write them?

Answer:

`True` and `False`

2. What are the three Boolean operators?

Answer:

There are three logical operators that are used to compare values. They evaluate expressions down to Boolean values, returning either `True` or `False` . These operators are `and`, `or`, and `not`

3. Write out the truth tables of each Boolean operator.

Answer:

| Expression | `True` $\land$ `True` | `True` $\land$ `False` | `False` $\land$ `True` | `False` $\land$ `False` |
| - | :-: | :-: | :-: | :-: |
| Evaluates to...  | __T__ | __F__ | __F__ | __F__ |

| Expression | `True` $\lor$ `True` | `True` $\lor$ `False` | `False` $\lor$ `True` | `False` $\lor$ `False` |
| - | :-: | :-: | :-: | :-: |
| Evaluates to...  | __T__ | __T__ | __T__ | __F__ |

| Expression | $\lnot$`True` | $\lnot$`False` |
| - | :-: | :-: |
| Evaluates to...  | __F__ | __T__ |


4. What do the following expressions evaluate to?

```py
(5 > 4) and (3 == 5)

not (5 > 4)

(5 > 4) or (3 == 5)

not ((5 > 4) or (3 == 5))

(True and True) and (True == False)

(not False) or (not True)
```

Answer:

```py
False

False

True

False

False

True
```

5. What are the six comparison operators?

Answer:

| Operator | Meaning |
| - | - |
| `==` | equal to|
| `!=` | not equal to|
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

6. What is the difference between the equal to operator and the assign-
ment operator?

Answer:

`==` test equality between two values

`=` assigns value to variable

7. Explain what a condition is and where you would use one.

Answer:

(two interpretations)

a) an expression in the context of control flow, e.g., `x > y`

Decision making in program execution. A conditional statement perform different computations or actions depending on whether a specific Boolean constraint evaluates to `True` or `False`. Conditional statements are handled by `if` statements in Python.


8. Identify the three blocks in this code:

```py
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```

Answer:

after `if`, `if`, `else`

NB: to instructor, this is nonsense code, emphasize that, if students ask

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

Answer:

```py
spam = 3
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')
```

10. What is an infinite loop and what keys can you press if your program is stuck in on?

Answer:

```py
while True:
    print('stuck in the loop')
```

KeyboardInterrupt: `ctrl + c` or `cmd + c`

11. What is the difference between break and continue statements?

Answer:

The `break` statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop. If the break statement is inside a nested loop (loop inside another loop), the `break` statement will terminate the innermost loop.

The `continue` statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.

12. What is the difference between `range(10)`, `range(0, 10)`, and `range(0, 10, 1)` in a for loop?

Answer:

There is no difference/explication of default parameter values

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

Answer:

```py
for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1
```

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

Answer:

```py
from spam import bacon

bacon()

# or

import spam

spam.bacon()

```

15. Look up the `round()` and `abs()` functions on the internet, and find out what they do. Test them in the interactive shell.

Answer:

```py
help(round)

Help on built-in function round in module builtins:

round(...)
    round(number[, ndigits]) -> number

    Round a number to a given precision in decimal digits (default 0 digits).
    This returns an int when called with one argument, otherwise the
    same type as the number. ndigits may be negative.

help(abs)

Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
```

16. Using `abs`, write some conditions that print `True` if the variable a is within 10\% of the variable b and `False` otherwise. Compare your implementation with your partner's: do you get the same answer for all possible pairs of numbers?

Answer:

```py
a = 5
b = 5.1

if abs(a - b) <= 0.1 * abs(b):
    print('True')
else:
    print('False')
```

```py
print(abs(a - b) <= 0.1 * abs(b))
```
