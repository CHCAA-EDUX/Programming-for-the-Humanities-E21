# PftH21 Curriculum #

## Lessons 1-13 ##

Each lesson consists of two elements:

1. Lecture, introduces a programming topic through a short presentation followed by a code-along session
2. Coding Café, are used for additional programming topics not directly related to Python (e.g., version control, bash scripting), research talks, and excercises/assignments.

---

### Lesson 1: File Management and Interactive Programming ###

__Time__ Monday, September 06, 0800-1000 (1200 w. café)  
__Location__ room 114B in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.


Introduces the imperative and procedural programming paradigms with Python. Topics included are basic math operators, variable assignment, PEP8, basic error handling.

#### Coding Café: Basic Python ####

Continues lesson 1 with a code-along

##### Reading #####

* A. Sweigart, 2019, chp 1: [Python Basics](https://automatetheboringstuff.com/2e/chapter1/)

---

### Lesson 2: Control Flow

__Time__ Monday, September 13, 0800-1000 (1200 w. café)  
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.


Introduces how to regulate the order in which a Python program's code executes. In programming, control flow is regulated by conditional statements, loops and function calls.

#### Coding Café: Coding challenges ####

In this coding café, you will solve [coding challenges](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/blob/main/exercises/excr_02_control_flow.md) about control flow in groups of two or four. Be sure that you can answer the [basic python challenges](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/blob/main/exercises/excr_01_basic_python.md) before you start.  
##### Reading #####

* Sweigart 2019, chp 2: [Flow Control](https://automatetheboringstuff.com/2e/chapter2/)

---

### Lesson 3: Functions and Modular Programming ###

__Time__ Monday, September 20, 0800-1000 (1200 w. café)  
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

Functions are bundles of organized and reusable code that run when called and require data and parameter (in most cases) that are used to control how a program's code executes. This lesson teaches modular programming focusing on the use of functions. In modular programming, we split code into seperate parts (i.e., modules) that are stored in seperate source files and can be reused across your projects.

#### Coding Café: Basic Unix

Using the Unix shell (command line interpreter) and terminal (text input/output environment) is an important tool for file managment, automation and client-server communication. This café will introduce basic commands and shell scripting.

In this coding café, we continue with the Unix shell and terminal focusing on automation and workflows.

##### Reading #####

* Sweigart 2019, chp 3: [Functions](https://automatetheboringstuff.com/2e/chapter3/)

##### Assignment 1 #####

[Assignment 1](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/blob/main/assignments/assign_01.md)

---

### Lesson 4: Lists and Dictionaries ###

__Time__ Monday, September 26, 0800-1000 (1200 w. café)  
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

Data type is an important concept in programming. Variables store data in different types that have type-specific methods associated with them. Python have multiple built-in data types, you have used simple data types like `str`, `int`, and `float` in the previous lessons; in this lesson we look at container-like data types that can be used to store and manipulate simple data types.

#### Coding Café: Basic Unix (Contd)

In this coding café, we continue with the Unix shell and terminal focusing on automation and workflows.

##### Reading ####

* Sweigart 2019, chp 4-5: [Lists](https://automatetheboringstuff.com/2e/chapter4/) and [Dictionaries and Structuring Data](https://automatetheboringstuff.com/2e/chapter5/)

---

### Lesson 5: String Manipulation ####

__Time__ Monday, October 04, 0800-1000 (1200 w. café)  
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

A string is a sequence of characters (character is a symbol). In Python 3, as in many other programming languages, strings, data type `str`, are arrays of bytes that represent unicode characters. In this lesson, we will look at string manipulation, which is the process of changing, parsing, splicing, pasting, or analyzing strings.

#### Coding Café: Fun with Information Retrieval ####

##### Reading #####

* Sweigart 2019, chp 6: [Manipulating Strings](https://automatetheboringstuff.com/2e/chapter6/)

##### Assignment 2 #####

* Assignment 2: Word Importance

---

### Lesson 6: Formats for Representing Structured Data (CSV and JSONS)

__Time__ Monday, October 11, 0800-1000 (1200 w. café)
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

In this lesson will cover how to work with CSV files and JSON data in Python.
CSV and JSON are data formats you most likely will encounter when doing data analysis.
CSV data (**C**omma **S**eparated **Va**lues) is widely used for tabular data. You might have seen it when working with a spreadsheet in Microsoft Excel.
JSON data (**J**ava**S**cript **O**bject **N**) is widely used for web applications and for communicating with servers. JSON data is structured in a nested hierarchy of key-value pairs.


#### Coding Café: Horoscope Challenge
In this coding café we will make a Horoscope Program and use the dataset `horoscopes.csv`.


##### Reading
* Sweigart 2019, chp 16: [Working with CSV files and JSON data](https://automatetheboringstuff.com/2e/chapter16/)


---

### Lesson 7: Classes and Object-Oriented Programming ###

__Time__ Monday, October 25, 0800-1000 (1200 w. café)
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

Object oriented programming (OOP) is a programming paradigm used to structure a program into bundles of related properties and behaviors into individual objects. Python classes provide all the standard features of OOP (inheritance mechanism, derived classes that override methods of base class, method call of base class). This lesson will teach you how to use OOP in Python to write a strategic code base that can be used and re-used across multiple projects.

#### Coding Café: Version Control ####

Version control with git is an invaluable tool for every coder, extending it with online repositories and social coding through GitHub completes the toolbox.

##### Reading

* [Version Control with Git: Get Started in less than 15 Minutes](https://towardsdatascience.com/version-control-with-git-get-started-in-less-than-15-minutes-696b4ce7ce92)

---

### Lesson 8: Classes and Object-Oriented Programming ###

__Time__ Monday, November 01, 0800-1000 (1200 w. café)
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

Object oriented programming (OOP) is a programming paradigm used to structure a program into bundles of related properties and behaviors into individual objects. Python classes provide all the standard features of OOP (inheritance mechanism, derived classes that override methods of base class, method call of base class). This lesson will teach you how to use OOP in Python to write a strategic code base that can be used and re-used across multiple projects.

#### Coding Café: Fun with Classes and OOP

##### Reading

* [Python Doc - Classes](https://docs.python.org/3/tutorial/classes.html)

##### Assignment 3 #####

* Class design and implementation

---

### Lesson 9: Web Scraping

__Time__ Monday, November 08, 0800-1000 (1200 w. café)
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

#### Coding Café

##### Reading
* Sweigart 2019, chp 12: [Web Scraping](https://automatetheboringstuff.com/2e/chapter12/)

---

### Lesson 10: Information Visualization

__Time__ Monday, November 15, 0800-1000 (1200 w. café)
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

#### Coding Café

##### Reading #####

#### Assignment 4 ####
* TBA

---

### Lesson 11: Introduction to Machine Learning and AI

__Time__ Monday, November 22, 0800-1000 (1200 w. café)   
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

Machine learning is an approach to programming that use data and learning systems to train algorithms (instead of specifying discrete steps in a programming space). This lesson is predominantly theoretical and will explain learning methods in machine learning as well as challenges such as black-box models and parity issues.
#### Coding Café

##### Reading

---

### Lesson 12: Supervised Machine Learning 1 ###

__Time__ Monday, November 29, 0800-1000 (1200 w. café)
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

#### Coding Café

##### Reading #####

#### Assignment 5 ####
* TBA

---

### Lesson 13: Supervised Machine Learning ###

__Time__ Monday, December 05, 0800-1000 (1200 w. café)
__Location__ room 138 in building [5008](https://www.au.dk/om/organisation/find-au/bygningskort/?b=5008), Helsingforsgade 8.

#### Coding Café

##### Reading


---
