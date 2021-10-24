# Exercises:  Object-Oriented Analysis and Design #

```yaml
Challenge: YOUML - You as an Object in Unified Modeling Language
Course: Programming for the Humanities E21
Tools: UML diagrams
Contact: kln@cas.au.dk
```

This challenge in not about code (at least not yer), but about designing templates that can be turned into code. Your task is to design several classes that can instantiate you in a particular user context of, for instance, a community ('Bouldering Club'), a business (e.g. 'Bookstore'), or a profession (e.g., 'BA Student'). Use UML-inspired diagrams to design your object template(s), box-and-pointer diagrams are sufficient.\*

We define an object as a _collection of data and associated behaviors_ and use dependency relations between types of objects (i.e., classes) to model complex objects. In Python _data_ is implemented as _attributes_ and _behavior_ as _methods_ (more about this in the next lesson).

## Object-Oriented Analysis ##

Start with (object-oriented) analysis, e.g., identify the objects and tasks that characterize you and your interactions in the specific context (e.g., bouldering amateur, `climb()` or `get_coffee()` ...). Keep attributes (data types) and dependencies (composition, inheritance) in mind , you are going to need them later, e.g., an 'amateur boulder' is also a _person_ and a person's _sex_ may matter in a bouldering competition, but not for a 'BA Student''s exam.

## Object-Oriented Design ##

Convert you OOA into a design of your object templates (classes) using UML. The result of this stage is an implementation specification in UML that can be implemented as a set of classes in Python. Don't worry about implementing them yet, but use your knowledge of Python as an inspiration for your visual formalization. Remember that in Python we use _method_ to implement behavior and _attributes_ for data. Methods are functions attached to objects and attributes are variables similarly attacted to objects, a 'BA student', for instance, may have the attribute `enrollment_year: datetime` and method `study(duration: int, intensity: str)`.  

NB: UML is supposed to facilitate, not restrict, design. Do not spend valuable time discussing the 'correct UML syntax', as long as you can use box-and-pointer diagrams to discuss your design, you're good.


\*) There are many tools for making UML diagrams, e.g., [StarUML](https://staruml.io/) and [UMLCD](https://github.com/xuyuan/pgf-umlcd) macros, but for this exercise box-and-pointer diagrams are sufficient (can be made in all office-style software, e.g., Google Docs or LibreOffice).

---

__Literature__

* Phillips, D. (2015). Python 3 object-oriented programming: Unleash the power of python 3 objects (Second edition). Packt Publishing, Chp 1.
