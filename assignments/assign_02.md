# Assignment 2: Word Importance #

In this assignement you have to work with `horoscope.csv` in order to learn how to identify important words (keywords and concepts) in a data set. The assignment will require you to combine your basic understanding of programming with python (control flow, functions, lists) with a string manipulation task inspired by information retrieval. You only have to solve two out of three problems, but if you feel up to it, go for all three.

You can download the `horoscope.csv` file [HERE](https://raw.githubusercontent.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/main/dat/horoscopes.csv).

## Format ##

For your assignment you should use the IMRaD format either in a separate report (pdf) combined with py scripts for your code OR in a markdown file with code blocks (similar to our [lessons](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/tree/main/lessons)). If you submit a markdown file do not turn it into a pdf.

An example of a markdown code block

```py
print('This is a Python code block')
```

### IMRaD format ###

IMRaD stands for _Introduction, Methods, Results, and Discussion_ and is often used for research papers and reports. The four parts refer to sections/headers that you should use. The _Introduction_ explains your (interpretation of the) problem (in this case the Assignment 2 tasks), _Methods_ how you approach the problem (what we have called Decomposition and Pattern Recognition), the _Results_ present your solution and validation, and, finally, the _Discussion_ your reflections on the problem and solution with respects to your field of study (what could your solution be used for, how should it be modified for better relevance etc).

### Submission ###

Again, two options a) text report in pdf accompanied by Python scripts OR b) markdown with text and Python code blocks. For both options you should use IMRaD formatting, first option only in report, and second option to structure the entire markdown file. __Please remember to hand in individual assignments even though you have developed you solution in a group__. The final exam, that is, your portfolio (3 assignments + 1 individual project), should reflect your individual contribution. Submit through Brightspace (either files or link to a public GitHub repository).

## Prerequisites ##

For the assignment, you need to load data from `horoscope.csv` available through [GitHub](https://raw.githubusercontent.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/main/dat/horoscopes.csv). To load the file in Python do the following:

```py
import pandas as pd
df = pd.read_csv('horoscopes.csv')
```

Assuming that you `horoscope.csv` file is in the same directory as your script. If your file is in another directory, ex. 'data/', you need to include the relative path:

```py
import pandas as pd # import pandas module
df = pd.read_csv('data/horoscopes.csv') # assign the dataframe with your data to variable 'df'
```

Csv files are tabular data (e.g., spreadsheets) and the horoscopes to be analyzed are in the `'horoscope-clean'` column. To extract that column and put it in the variable `texts` as a list data type use the following statement

```py
texts = df['horoscope-clean'].values
```

To test if you have extracted the data correctly, you can check the length of the list:

```py
print(len(texts))
```

Which should return `12946`, meaning that you have 12946 horoscopes. If you print the first element in the list, `print(texts[0])`, you should see that (notice that there are no punctuation):

```sh
You re not the sort to play safe and even if you have been a bit more cautious than usual in recent weeks you will more than make up for it over the next few days Plan your new adventure today and start working
on it tomorrow
```

## Problem 1: With or without function words ##

Compare the top 100 most frequent words in all horoscopes with and without stopwords (i.e. function words), what seems to be the most striking differences? You should include your stopword list (or a link to) in the answer. You can use a wordcloud to visualize the comparison (requires that you `pip install wordcloud` from the terminal) 

```py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wordcloud = WordCloud(stopwords=stopwordlist,background_color="white").generate(texts)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout()
plt.savefig('wordcloud.png')
```

or you can use the following set functions to compare lists of words:

```py

def intersection(lst1, lst2):
    """ returns the intersection between two lists
    e.g., lst1 = [1,2,3] and lst2 = [2,3,4], then the intersection is [2,3]
    """
    return list(set(lst1) & set(lst2))

def difference(lst1, lst2):
    """ returns the asymmetric difference between two lists
    e.g., lst1 = [1,2,3] and lst2 = [2,3,4], the the difference (for lst1) is [1]
    """
    return list(set(lst1).difference(set(lst2)))
```

## Problem 2: TF-IDF Weighting ##

Compare top 100 most frequent words in all horoscopes based on word counts and TF-IDF weighting of the term frequencies, what seems to be the most striking differences, how can you explain them, what happens if you apply a stopword list? Y0u can use wordclouds or set functions from Problem 1 for the comparison (or any other comparison you may prefer)?

## Problem 3: Sign-specific indexing ##

Compare top 200 most frequent words for at least three different Zodiac signs (ex. virgo, leo, pisces) using the `difference` set function from Problem 1. Are there any apparent characteristics/distinct differences between the signs?

To extract subsets of the data based on a specific zodiac sign, use the following indexing technique. First select the relevant sign:

```py
signs = list(set(df['sign'].values))
print(signs)
```

Which should result in the following lists

```sh
['libra', 'virgo', 'taurus', 'capricorn', 'aquarius', 'pisces', 'leo', 'gemini', 'scorpio', 'sagittarius', 'aries', 'cancer']
```

To extract horoscopes from 'virgo' use boolean indexing in the dataframe column `horoscope-clean`

```py
idxs = df['sign'] == 'virgo'
texts = df['horoscope-clean'].loc[idxs].values
```

Or for 'pisces' use

```py
idxs = df['sign'] == 'pisces'
texts = df['horoscope-clean'].loc[idxs].values
```
