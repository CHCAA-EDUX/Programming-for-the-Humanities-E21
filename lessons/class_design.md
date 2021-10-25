# Classes in Python - OOD reference #

This lesson is a reference file for [Hello, my name is <name>: An introduction to OOP in Python with UML](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/blob/main/slides/pfth_21e_07.pdf)

Object-oriented design (OOD) is the process of converting such requirements into an implementation specification. The designer must name the objects, define the behaviors, and formally specify which objects can activate specific behaviors on other objects. The design stage is all about how things should be done. The output of the design stage is an implementation specification. If we were to complete the design stage in a single step, we would have turned the requirements defined during object-oriented analysis into a set of classes and interfaces that could be implemented in (ideally) any object-oriented programming language. OOP then is the process of converting this perfectly defined design into a working program (modified from Phillips 2015, Chp 1).

We are going to create a set of classes of which [Kristoffer L Nielbo](https://pure.au.dk/portal/en/persons/kristoffer-laigaard-nielbo(aef8887c-d4e9-4270-9031-1a15553f5590).html) (KLN) is an instance. KLN is a principal investigator that is a researcher that is a person (see UML diagrams in slides).

Create a file `class_intro.py`.

We start by implementing a `Person` class with three attributes, one required parameter `name` and two optional `age` and `sex`.

```py
class Person:
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
```

Run in interactive mode with `i` flag

```sh
$ python -i class_intro.py
>>> kln = Person('Kristoffer L. Nielbo', age=44, sex="male")
>>> print(f'{kln.name} is a {kln.sex} specimen of {kln.age} years')
Kristoffer L. Nielbo is a male specimen of 44 years
```

Let us add some behavior, start with 'get()' functionality to produce surname

```py
class Person:
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
    
    def getSurname(self):
        return self.name.split()[-1]
```

then we produce year of birth. Notice that we introduce a dependency `datetime` to caclulate age.

```py
import datetime

class Person:
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
    
    def getSurname(self):
        return self.name.split()[-1]
    
    def getBirthyear(self):
        now = datetime.datetime.now()
        return now.year - self.age
```

and run from terminal

```sh
$ python -i class_intro.py
>>> kln = Person('Kristoffer L. Nielbo', age=44, sex="male")
>>> print(f'Mr. {kln.getSurname()} was born in {kln.getBirthyear()}')
Mr. Nielbo was born in 1977
```

We can also add 'set()' to let a Persons respond emotionally to a context

```py
class Person:
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
    
    def getSurname(self):
        return self.name.split()[-1]
    
    def getBirthyear(self):
        now = datetime.datetime.now()
        return now.year - self.age
    
    def setMood(self, happy=False):
        if happy:
            self.mood = 'happy'
            print(f'{self.name.split()[0]}: I have no regrets over past mistakes')
        else:
            self.mood = 'angry'
            print(f'{self.name.split()[0]}: #@*%')
```

and test in terminal, setting our subject's mood to 'happy'

```sh
$ python -i class_intro.py
>>> kln = Person('Kristoffer L. Nielbo', age=44, sex="male")
>>> kln.setMood(happy=True)
Kristoffer: I have no regrets over past mistakes
```

__Advanced topic__:

We can overload operators using dunder methods - in this case we override the printable representational string of the given Person instance with `repr`. For more detail on operator and function overloading, see [article](https://realpython.com/operator-function-overloading/).

Before operator overloading with `repr`

```sh
>>> print(kln)
<__main__.Person object at 0x7f6bb8c7d860>
```

```py
class Person:
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
    
    def getSurname(self):
        return self.name.split()[-1]
    
    def getBirthyear(self):
        now = datetime.datetime.now()
        return now.year - self.age
    
    def setMood(self, happy=False):
        if happy:
            self.mood = 'happy'
            print(f'{self.name.split()[0]}: I have no regrets over past mistakes')
        else:
            self.mood = 'angry'
            print(f'{self.name.split()[0]}: #@*%')
        
    def __repr__(self):
        return f'[Person: {self.name}, {self.age}, {self.sex}]'
```

After having change the printable representational string

```sh
$ python -i class_intro.py
>>> kln = Person('Kristoffer L. Nielbo', age=44, sex="male")
>>> print(kln)
[Person: Kristoffer L. Nielbo, 44, male]
```

Now we create a researcher subclass of person. Following our analysis, a researcher has a paygrade (it is a profession) and research areas. We use integers to model pay (in 'squishies') and a list of strings for research areas. We provide default values for both parameters.

```py
class Researcher(Person):
    def __init__(self, pay=10, areas=['research'],  **kwargs):
        super(Researcher, self).__init__(**kwargs)
        self.pay = pay
        self.areas = areas
```

Notice we use `super()` to delegate an object to a parent class and thereby to avoid referring to the base class (Person) explicitly. The main advantage comes with multiple inheritance.

```sh
$ python -i class_intro.py
>>> kln = Researcher(
...         name='Kristoffer L. Nielbo',
...         age=44, sex="male",
...         areas=['culture analytics', 'humanities computing']
...         )
>>> for area in kln.areas:
...     print(f'Dr. {kln.getSurname()} works in {area}')
...
Dr. Nielbo works in culture analytics
Dr. Nielbo works in humanities computing
```

We also want to be able to give researchers a bonus (if they perform well). We add a method `giveBonus()` that allow us to add bonus squishies.

```py
class Researcher(Person):
    def __init__(self, pay=10, areas=['research'],  **kwargs):
        super(Researcher, self).__init__(**kwargs)
        self.pay = pay
        self.areas = areas

    def giveBonus(self, bonus):
        self.pay = self.pay + bonus
```

Now let us give instantiate our test subject and give him a bonus of 1 squishy.

```sh
$ python -i class_intro.py
>>> kln = Researcher(
...         name='Kristoffer L. Nielbo',
...         age=44, sex="male",
...         areas=['culture analytics', 'humanities computing']
...         )
>>> kln.giveBonus(1)
>>> print(f'Paygrade of {kln.name} after a bonus is {kln.pay} squishies')
Paygrade of Kristoffer L. Nielbo after a bonus is 11 squishies
```

__Advanced topic__:

Finally, we want to create our researcher subclass `PrincipalInvestigator` using multiple inheritance. PI's are like researchers, but they also have to manage a research group (i.e., a laboratory), which can be taxing on the nerves. We therefore want to give an additional bonus relative to the pain and suffering of the PI's job `painandsuffering`. Notice that we use function overloading of `giveBonus` to implement this behavior. 

```py
class PrincipalInvestigator(Researcher):
    def giveBonus(self, bonus, painandsuffering=.10):
        Researcher.giveBonus(self, bonus * (1 + painandsuffering))
```

And finally we can instantiate the test subject as a principal investigator, give him a bonus and and set his mood accordingly.

```sh
$ python -i class_intro.py
kln = PrincipalInvestigator(
        name='Kristoffer L. Nielbo', 
        age=44, sex="male", 
        areas=['culture analytics', 'humanities computing']
        )
>>> kln.giveBonus(1)
>>> kln.setMood(happy=True)
Kristoffer: I have no regrets over past mistakes
```

---

__Literature__

* Phillips, D. (2015). Python 3 object-oriented programming: Unleash the power of python 3 objects (Second edition). Packt Publishing, Chp 1.
