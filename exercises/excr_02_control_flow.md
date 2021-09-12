# Exercises: Control Flow #

Solve the following 'Pair programming', 'Check your understanding', and 'Practice questions' challenges in groups of two or four.

## Pair programming ##

Conting vowels:

1. Write a loop that counts the number of vowels in a character string.
2. Test it on a few individual words and full sentences.
3. Once you are done, compare your solution to your neighbor pair's. Did you make the same decisions about how to handle the letter ‘y’ (which some people think is a vowel, and some do not)?

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

## Practice questions ##

1. What are the two values of the Boolean data type? How do you write them?

2. What are the three Boolean operators?

3. Write out the truth tables of each Boolean operator.

4. What do the following expressions evaluate to?

```py
(5 > 4) and (3 == 5)

not (5 > 4)

(5 > 4) or (3 == 5)

not ((5 > 4) or (3 == 5))

(True and True) and (True == False)

(not False) or (not True)
```

5. What are the six comparison operators?

6. What is the difference between the equal to operator and the assign-
ment operator?

7. Explain what a condition is and where you would use one.

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

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

10. What is an infinite loop and what keys can you press if your program is stuck in on?

11. What is the difference between break and continue statements?

12. What is the difference between `range(10)`, `range(0, 10)`, and `range(0, 10, 1)` in a for loop?

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

15. Look up the `round()` and `abs()` functions on the internet, and find out what they do. Test them in the interactive shell.

16. Using `abs`, write some conditions that print `True` if the variable a is within 10\% of the variable b and `False` otherwise. Compare your implementation with your partner's: do you get the same answer for all possible pairs of numbers?
