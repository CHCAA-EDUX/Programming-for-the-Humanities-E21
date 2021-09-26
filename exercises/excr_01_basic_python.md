# Exercises for Basic Python Lesson #

## Pair programming ##

Write a program, `hello.py` that that says hello and asks for name

```py
print('Hello, world!')
print('What is your name?')
name = input()
print(f'Good to meet you {name}')

print(f'The length of your name is {len(name)}')

print('What is your age?')
age = input()
print(f'You will be {int(age) + 1} in a year')
```

## Check your understanding ##

1: What values do the variables `mass` and `age` have after each of the following statements? Test your answer by executing the lines.

```py
1 mass = 47.5
2 age = 122
3 mass = mass * 2.0
4 age = age - 20
```

Answer:

1. `mass` holds a value of 47.5, `age` does not exist
2. `mass` still holds a value of 47.5, `age` holds a value of 122
3. `mass` now has a value of 95.0, `age`'s value is still 122
4. `mass` still has a value of 95.0, `age` now holds 102

2: Sorting Out References. Python allows you to assign multiple values to multiple variables in one line by separating the variables and values with commas. What does the following program print out?

```py
first, second = 'James', 'Kirk'
third, fourth = second, first
print(third, fourth)
```

Answer:

- `Kirk James`

3: Seeing Data Types. What are the data types of the following variables?

```py
planet = 'Earth'
apples = 5
distance = 10.5
```

Answer:

```py
type(planet)
type(apples)
type(distance)
```

```py
<class 'str'>
<class 'int'>
<class 'float'>
```

## Practice questions ##

1: Which of the following are operators, and which are values?

```py
*
'hello'
-88.8
-
/
+
5
```

Answer:

- operator
- value
- value
- operator
- operator
- operator
- value

2: Which of the following is a variable, and which is a string?

```py
spam
'spam'
```

Answer:
- `spam` is a variable and `'spam'` is a string

3: Name three data types

Answer:
- sting
- integer
- float

4: What is an expressions made up of? What fo all expressions do?

Answer:
- An expression is an instruction that combines values and operators and always evaluates down to a single value.


5: What is a statement, e.g., assignment statement `var = 10`

Answer:

- A statement is an instruction that the Python interpreter can execute. We have seen two kinds of statements: print and assignment. When you type a statement on the command line, Python executes it and displays the result, if there is one. The result of a print statement is a value.
- Statements represent an action or command e.g print statements, assignment statements. Expression is a combination of variables, operations and values that yields a result value. An expression is something that can be reduced to a value, for example `1+3` is an expression, but `foo = 1+3` is not.

6: what does the variable `spock` contain in the following code

```py
spock = 20
spock + 1
```

7: What should the following two expressions evaluate to

```py
'spam' + 'spamspam'
'spam' * 3
```

8: Why is `spock` a valid variable name and 100 invalid

Answer:

- one word with no spaces
- only use letters, numbers and underscore
- cannot begin with number

| Valid | Invalid |
| --- | --- |
| snake_case | snake-case |
| camelBack | camel back |
| wnumber23 | 23wnumber |
| _23 | 23 |
| TOTAL_SUM | TOTAL_$UM |
| hello | 'hello' |

9: What three functions can be used to get the integer, floating-point numner, string version of a value

Answer:

- `int()`
- `float()`
- `str()`