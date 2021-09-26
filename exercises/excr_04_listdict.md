# Exercises for Functions Lesson #

## Pair programming ##

</details>

<br /> 

</details>

<details>

<summary> 

Take the following nested list 

```py
>>> fridge = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]
```

and create a function that returns a _flat list_:

```py
['pepper', 'zucchini', 'onion', 'cabbage', 'lettuce', 'garlic', 'apple', 'pear', 'banana']
```

</summary>

_Answer_

```py
def flatten(lst):
    """
    Flatten list

    Input:
        - lst, a nested list (one level of nesting only)
    """
    flat_list = list()
    for sublst in lst:
        for item in sublst:
            flat_list.append(item)
    
    return flat_list

# OR with a list comprehension

def flatten(lst):
    return [item for sublst in lst for item in sublst]


fridge = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]

flat_fridge = flatten(fridge)
print(flat_fridge)
```

</details>

## Check your understanding ##


</details>

<br /> 

</details>

<details>
<summary>

1. Take the following two lists as input

```py
value_list = ['Spock', 25 , 'TPol', 23 ]
key_list = ['name', 'age']
```

Write a script that maps keys onto values in dictionaries nested in a list such that it outputs

```py
[{'name': 'Spock', 'age': 25 }, {'name': 'TPol', 'age': 23}]
```
</summary>

_Answer_

```py
value_list = ['Spock', 25 , 'TPol', 23 ]
key_list = ['name', 'age']

n = len(value_list)
result = []
for i in range(0, n, 2):
    result.append({key_list[0]: value_list[i], key_list[1]: value_list[i+1]})

print(result)
```

</details>


</details>

<br /> 

</details>

<details>
<summary> `+` usually means addition, but when used on strings or lists, it means 'concatenate'. Given that, what do you think the multiplication operator `*` does on lists? In particular, what will be the output of the following code? 
  
```py
counts = [2, 4, 6, 8, 10]
repeats = counts * 2
print(repeats)
```

* `[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]`
* `[4, 8, 12, 16, 20]`
* `[[2, 4, 6, 8, 10],[2, 4, 6, 8, 10]]`
* `[2, 4, 6, 8, 10, 4, 8, 12, 16, 20]`

</summary>

* `[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]`

</details>

---

## Practice questions ##


<br /> 

</details>

<details>
  <summary> 1. What is []?</summary>

An empty `list`. In Python square brackets are used to open and close a list object.

</details>


<br /> 

</details>

<details>
  <summary> 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume `spam` contains [2, 4, 6, 8, 10].)</summary>

`spam[2] = 'hello'` 

</details>



3. For the following three questions, let’s say spam contains the list `['a', 'b', 'c', 'd']`.

<br /> 

</details>

<details>
  <summary> 3.1. What does `spam[int(int('3' * 2)` // 11)] evaluate to?</summary>

`'d'`

</details>


<br /> 

</details>

<details>
  <summary> 3.2. What does spam[-1] evaluate to? </summary>

`'d'`

</details>


<br /> 

</details>

<details>
  <summary> 3.3.What does spam[:2] evaluate to? </summary>

`['a', 'b']`

</details>



4. For the following three questions, let’s say `ham` contains the list
`[3.14, 'cat', 11, 'cat', True]`.

</details>


<br /> 

</details>

<details>
  <summary> 4.1 What does ham.index('cat') evaluate to? </summary>

`1`, The `index()` method returns the first index of the specified element in the list. Use optional `start` and `end` parameters in `list.index(element, start, end)` to search from and up to specific index.

</details>


</details>

<br /> 

</details>

<details>
  <summary> 4.2. What does ham.append(99) make the list value in `ham` look like? </summary>

`[3.14, 'cat', 11, 'cat', True, 99]`, the `.append()` method adds a single item to the existing list. It doesn't return a new list of items but will modify the original list by adding the item to the end of the list.

</details>

</details>

<br /> 

</details>

<details>
  <summary> 4.3. What does ham.remove('cat') make the list value in `ham` look like? </summary>

`[3.14, 11, 'cat', True]`, the `remove()` method takes a single element as an argument and removes it from the list. If the element doesn't exist, it throws `ValueError`.

</details>


</details>

<br /> 

</details>

<details>
  <summary> 5. What are the operators for list concatenation and list replication?
 </summary>

*  `+` concatenation
* `*` replication

(similar to string concatenation and replication)

</details>


</details>

<br /> 

</details>

<details>
  <summary> 6. What is the difference between the append() and insert() list methods? </summary>

The `insert(i, elem)` method adds item `elem` to a list at a specific position `i` in a list, while `append(elem)` adds an item `elem` to the end of the list.

</details>


</details>

<br /> 

</details>

<details>
  <summary> 7. What are two ways to remove values from a list? </summary>

* `mylist.remove(elem)`
* `del mylist[i]` 

and 

* `mylist.pop(i)`, removes value by index i and return value
* `mylist.clear()`, removes all values from list

</details>


</details>

<br /> 

</details>

<details>
  <summary> 8. Name a few ways that list values are similar to string values. </summary>

both data types are sequential data types, so

* they are ordered in a defined sequence
* the elements can be accessed via indices
* the meaning of `+` and `*` is the same (concatenation and replication)

</details>


</details>

<br /> 

</details>

<details>
  <summary> 9. What is the difference between lists and tuples? </summary>

The `list` data type is a mutable object, while the `tuple` is an immutable and fixed size object. This difference means that Python must allocate an extra memory block to extend the list obect when created, which makes lists less memory efficient than tuples. 

</details>


</details>

<br /> 

</details>

<details>
  <summary> 10. How do you type the tuple value that has just the integer value 42 in it? </summary>

`(42)`

</details>


</details>

<br /> 

</details>

<details>
  <summary> 11. How can you get the tuple form of a list value? How can you get the list form of a tuple value? </summary>

`tuple(mylist)` and `list(mytuple)`

</details>


</details>

<br /> 

</details>

<details>
  <summary> 12. Variables that 'contain' list values don't actually contain lists directly. What do they contain instead? </summary>

References to objects in memory. When the '=' operator is used to copy a mutable object, it does not create a new object, it only creates a new variable that share reference to the original object.

</details>


</details>

<br /> 

</details>

<details>
  <summary> 13. What is the difference between copy.copy() and copy.deepcopy()? </summary>

shallow copy (`copy()`): will create new and independent object with same content
deep copy (`deepcopy()`): creates a new object and recursively adds the copies of nested objects present in the original elements.

</details>


</details>

<br /> 

</details>

<details>
  <summary> 14. What does the code for an empty dictionary look like? </summary>

`{}`

</details>


</details>

<br /> 

</details>

<details>
  <summary> 15. What does a dictionary value with a key 'foo' and a value 42 look like? </summary>

`{'foo': 42}`

</details>


</details>

<br /> 

</details>

<details>
  <summary> 16. What is the main difference between a dictionary and a list?
 </summary>

Both are collections, but the `list` data type is an ordered sequence of elements, while the `dict` data type is an unordered set. The `dict` elements therefore are accessed via keys, while the 'list' elements via position (index).  

</details>


</details>

<br /> 

</details>

<details>
  <summary> 17. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
 </summary>

The Python interpreter returns a `KeyError`

</details>


</details>

<br /> 

</details>

<details>
  <summary> 18. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
 </summary>

They are equivalent in Python 3, they both the the existence of a key in dictionary, but the pattern `key in dict` is (historically) more correct.

</details>


</details>

<br /> 

</details>

<details>
<summary> 
19. What is a shortcut for the following code? 

```py
if 'color' not in spam:
    spam['color'] = 'black'
```
</summary>

use the `setdefault(key, value)` method, `spam.setdefault('color', 'black')`

</details>


</details>

<br /> 

</details>

<details>
  <summary> 20. What module and function can be used to 'pretty print'
dictionary values?
 </summary>

`pprint`

</details>
