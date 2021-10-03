# Exercises for String Lesson #

## Pair programming ##

Create a bag-of-word representation of these three texts:

```py
texts = [
    "cyberspace a consensual hallucination experienced daily by billions of legitimate operators in every nation",
    "the internet is becoming the town square for the global village of tomorrow",
    "cyberspace is the funhouse mirror of our own society",
]
```

What pair of text is most similar and why?

</details>

<br /> 

</details>

<details>
  <summary> [Answer] </summary>

```py
from scipy import spatial

def tokenizer(text):
    return text.split()

def word_count(text, sort = True):
    """ count words
    """
    counter = {}
    for word in tokenizer(text):
        counter.setdefault(word, 0)
        counter[word] = counter[word] + 1
    
    return counter

def list_to_dtm(corpus):
    """ build document term matrix from list of string documents
    """
    wc = word_count(' '.join(corpus))
    lexicon = sorted(list(wc.keys()))
    
    dtm = []
    for content in corpus:
        document = [0 for _ in lexicon]
        wc = word_count(content)
        for (i, word) in enumerate(lexicon):
            if word in wc:
                document[i] = wc[word]
        
        dtm.append(document)
    
    return dtm, lexicon

texts = [
    "cyberspace a consensual hallucination experienced daily by billions of legitimate operators in every nation",
    "the internet is becoming the town square for the global village of tomorrow",
    "cyberspace is the funhouse mirror of our own society",
]
dtm, lexicon = list_to_dtm(texts)

print('[INFO] Cosine similarity for pairwise document comparison')
print('[INFO] Document 1 and 2:')
print(1 - spatial.distance.cosine(dtm[0],dtm[1]))
print('[INFO] Document 1 and 3:')
print(1 - spatial.distance.cosine(dtm[0],dtm[2]))
print('[INFO] Document 2 and 3:')
print(1 - spatial.distance.cosine(dtm[1],dtm[2]))
```
</details>

---

## Check your understanding ##

1. A section of an array is called a slice. We can take slices of character strings as well:

```py
element = 'oxygen'
print(f'first three characters: {element[0:3]}')
print(f'last three characters: {element[3:6]}')
```

```py
first three characters: oxy
last three characters: gen
```

* What is the value of `element[:4]`? What about `element[4:]`? Or `element[:]`?
* What is element[-1]? What is element[-2]?
* Given those answers, explain what element[1:-1] does.


</details>

<br /> 

</details>

<details>
  <summary> [Answer] </summary>

```py
oxyg
en
oxygen
```

```py
n
e
```


Creates a substring from index 1 up to (not including) the final index, effectively removing the first and last letters from `oxygen`

</details>

---

2. Strings as sequences

Given the following loop:

```py
word = 'oxygen'
for char in word:
    print(char)
```

How many times is the body of the loop executed?

* 3 times
* 4 times
* 5 times
* 6 times

</details>

<br /> 

</details>

<details>
  <summary> [Answer] </summary>

The body of the loop is executed 6 times.

</details> 

---

3. Given the string `'gnop gnip'` write a for loop what mirrors the string
</details>

<br /> 

</details>

<details>
  <summary> [Answer] </summary>

```py
reverse_string = ''
for char in 'gnop gnip':
    reverse_string = char + reverse_string
```

</details>


---

## Practice questions ##

1. What are escape characters?
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>
  In Python, '\' is the escape character that, among other things, is used to represent special whitespace characters.
</details>

---

2. What do the `\n` and `\t` escape characters represent?
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

ASCII Linefeed (adds new line) and ASCII Horizontal Tab (TAB), for a complete list see <a href="https://docs.python.org/3/reference/lexical_analysis.html#strings">Python documentation</a>

</details>

---

3. How can you put a `\` backslash character in a string?
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

```py
print('a backslash: \\')
print(r"another backslash '\'")
```

</details>

---

4. The string value `"Howl's Moving Castle"` is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

Because a string is a sequence of (Unicode) characters wrapped inside single, double, or triple quotes. In the example double quotes are used to create the string expression.

</details>

---

5. If you don’t want to put `\n` in your string, how can you write a string with newlines in it?
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

```py
multiline = """line 0
        line 1
        ...
        line n
        """
print(multiline)
```

</details>

---

6. What do the following expressions evaluate to?

```py
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
```
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

```py
'e'
'Hello'
'Hello'
'lo, world!'
```

</details>

---

7. What do the following expressions evaluate to?
```py
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
```
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

```py
'HELLO'
True
'hello'
```

</details>

---

8. What do the following expressions evaluate to?
```py
'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
```
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

```py
['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.'] 
'There-can-be-only-one.'
```

</details>

---

9. What string methods can you use to right-justify, left-justify, and center
a string?
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

```py
string.rjust()
string.ljust()
string.center()
```

</details>

---

10. How can you trim whitespace characters from the beginning or end of
a string?
</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

```py
string.strip()
string.lstrip()
string.rstrip()

```
</details>