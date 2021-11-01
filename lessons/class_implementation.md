# Classes in Python #

This is an introduction to Object-Oriented Programming and classes in Python

Learning goals:

* How to create classes and instantiate objects in Python
* How to add attributes and behaviors to Python objects
* How to organize classes into packages and modules

## Creating a class ##

Use the `class` keyword to define a class and end with `:`. Notice the naming rule, we reserve CamelCase for class defintion accoring to PEP 8.

Create a file `persons.py` and define your first class without any data or behavior.

```py
class Person:
    pass
```

Open the terminal and instantiate the class in interactive mode

```sh
$ python -i persons.py
>>> o = Person()
>>> print(o)
<class '__main__.Person'>
```

Similar to a function call, but Python 'knows' that we are calling a class, not a function.

### Adding attributes ###

With python objects, we can add attributes interactively using dot notation `<object>.<attribute> = <value>`.

```sh
>>> class Person:
...     pass
...
>>> p1 = Person()
>>> p2 = Person()
>>> p1.name = 'Peter'
>>> p1.sex = 'male'
>>> p2.name = 'Wendy'
>>> p2.sex = 'female'
>>> print(p1.name, p1.sex)
Peter male
>>> print(p2.name, p2.sex)
Wendy female
>>> dir(p1)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'sex']

```

More formally, we can add attributes to our class.
---
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

## Entry point function ##

 The `main()` function is conventionally the entry point, where a Python program starts its execution. It enables high-level organization of the program's functionality, and typically has access to the command arguments given to the program when it was executed. 

Finalize your persons.py script by adding a `main()` function and using the `__main__` special name for the top-level environment of the program.

 ```py
def main():
    kln = PrincipalInvestigator(
        name='Kristoffer L. Nielbo', 
        age=44, sex="male", 
        areas=['culture analytics', 'humanities computing']
        )
    kln.giveBonus(1)
    kln.setMood(happy=True)

if __name__ == '__main__':
    main()
 ```

---

__Literature__

* Phillips, D. (2015). Python 3 object-oriented programming: Unleash the power of python 3 objects (Second edition). Packt Publishing, Chp 1.
