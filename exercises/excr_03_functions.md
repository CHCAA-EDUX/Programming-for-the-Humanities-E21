# Exercises for Functions Lesson #

## Pair programming ##

Create a function that takes a list as input, ex. `[1, 1, 2, 3, 5, 8]`
and returns the list in reverse order, ex, `[8, 5, 3, 2, 1, 1]`.

```py
def reverser(lst):
    return lst[::-1]

def reverser(lst):
    res = list()
    for i in range(len(lst) - 1, -1, -1):
        res.append(lst[i])
    return res
```


## Check your understanding ##

__Combining Strings__

'Adding' two strings produces their concatenation: `a + b` is `ab`. Write a function called `fence()` that takes two parameters called `original` and `wrapper` and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:

```py
>>> print(fence('name', '*'))
```

and the output should be

```py
*name*
```

Answer:
```py
def fence(original, wrapper):
    return wrapper + original + wrapper
```

__Return versus print__

Note that `return` and `print()` are not interchangeable. `print()` is a function that prints data to the screen. It enables us, users, see the data. The `return` statement, on the other hand, makes data visible to the program. Let’s have a look at the following function:

```py
def add(a, b):
    print(a + b)
```

What will we see if we execute the following commands?

```py
A = add(7, 3)
print(A)
```

Answer:

Python will first execute the function `add()` with `a = 7` and `b = 3`, and, therefore, print 10. However, because function `add()` does not have a line that starts with `return` (no return 'statement'), it will, by default, return nothing which is called `None`. Therefore, A will be assigned to `None` and the last line (`print(A)`) will print `None`. As a result, we will see:

```py
10
None
```

__Selecting Characters From Strings__

If the variable `s` refers to a string, then `s[0]` is the string’s first character and `s[-1]` is its last. Write a function called `outer()` that returns a string made up of just the first and last characters of its input. A call to your function should look like this:

```py
>>> print(outer('helium'))
```

and output 

```py
hm
```

Answer:

```py
def outer(input_string):
    return input_string[0] + input_string[-1]
```

## Practice questions ##

In your answers to practice questions, try to use code to illustrate your answer.


1: Why are the advantageous of functions, and more generally, modular programming?

Answer: modular/manageble & reusable code

2: When does the code in a function execute: during function definition or function call?

Answer: function cal

3: What statement creates a function?

Answer: the `def` statement works as follows. `def` is the keyword for defining a function. The function name is followed by parameter(s) in (). The colon : signals the start of the function body, which is marked by indentation. Inside the function body, the return statement determines the value to be returned. 

4: What is the difference between a function and a function call?

Answer: A function call means invoking or calling that function. Unless a function is called there is no use of that function. The difference between the function and function call is, _a function is procedure to achieve a particular result while function call is using this function to achive that task_.

5: How many scopes are there in Python?

Answer: two or four depending on how you cound

6: What happens to a variable in local scope, when the function call returns?

Answer: deleted

7: What is a return value? Can a return value be part of an expression?

Answer: The `return` statement is a special statement that you can use inside a function or method to send the function's result back to the caller. A return statement consists of the return keyword followed by an optional return value. The return value of a Python function can be any Python object.

Yes, because an expression is just a representation of a value. Expressions are composed of values and operators. A function call can be used in an expression because the call evaluates to its return value.

```py
def hello(name):
    return name

print(hello('Spock'))
```

8: If a function lacks a return statement, what is the return value of the function call?

Answer: `None`

9: What keyword allow you to update a global variable in a function?

Answer: `global`

10: What does `None` mean?

Answer: null value

11: What does the `import numpy` statement do?

Answer: import the objects in the numpy namespace

12: If you have a function named `randint()` and a module named `random`, how would you import and call `randint`?

Answer: `random.randint()`

13: How do you prevent a program from crashing, when it gets an error?

Answer: `try - except`, `assert`

14: What constitutes the `try` clause? What constitutes the `except` clause?

Answer:

In the try clause, all statements are executed until an exception is encountered. except is used to catch and handle the exception(s) that are encountered in the try clause. else lets you code sections that should run only when no exceptions are encountered in the try clause.

* `try` keyword, `:`, indentation and code to be executed
* `except` keyword, `:`, indentation and code to be executed when exeption occurs