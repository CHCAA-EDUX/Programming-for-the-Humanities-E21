# Assignment 5: Horoscope Classification with scikit-learn #

In this assignment you have to use your knowledge of strings, tabular data, and machine learning to train a horoscope classifier in Python 3. 

The assignment has three problems and you you have to _solve at least two_. You should use the horoscope data available [here](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/blob/main/dat/horoscopes.csv). By default, the assignments assume that you use `scikit-learn`, but if you prefer to use another machine learning library that is a fully acceptable solution.

In your submission, please discuss what your results mean for the genre of horoscopes (what can we learn about horoscopes from the study).

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

## 1. Binary classification ##

Train a binary (two-label) Naive Bayes classifier that predicts two classes (e.g., `virgo` and `pisces`) of the `sign` variable from the horosope content of `horoscope`. Knowing that the baseline (Zero Rate) accuracy is approximately 50%, discuss the performance (accuracy and confusion matrix) of your classifier. 

To extract subsets of the data based on a specific zodiac sign, use the following indexing technique. First select the relevant sign:

```py
signs = list(set(df['sign'].values))
print(signs)
```

Which should result in the following lists

```sh
['libra', 'virgo', 'taurus', 'capricorn', 'aquarius', 'pisces', 'leo', 'gemini', 'scorpio', 'sagittarius', 'aries', 'cancer']
```

To extract horoscopes from 'virgo' use boolean indexing in the dataframe column `horoscope`

```py
idxs = df['sign'] == 'virgo'
corpus = df['horoscope'].loc[idxs].values
```

Or for 'pisces' use

```py
idxs = df['sign'] == 'pisces'
corpus = df['horoscope'].loc[idxs].values
```

To place two or more signs in the same variable use this pattern

```py
idxs0 = data['sign'] == 'virgo'
idxs1 = data['sign'] == 'leo'
idxs = idxs0.values + idxs1.values
corpus = df['horoscope'].loc[idxs].values
```

## 2. Effects of preprocessing ##

Preprocessing your natural language data before training a classifier can improve performance considerably, Look at the documentation for the `CountVectorizer()` function and use some of the parameters to preprocess your horoscope data. Then train two binary classifier and discuss one with and one without preprocessing and compare the performance.

Example of pruning the document-term matrix and removin stopwords for English with the `CountVectorizer()`'s parameters

```py
cv = CountVectorizer(max_df=0.9, min_df=5, stop_words='english')
X = cv.fit_transform(corpus.values).toarray()
```

## 3. Multilabel Classification ##

Train a multilabel Naive Bayes classifier that predicts all twelve classes of the `sign` variable from the horosope content of `horoscope`. Knowing that the baseline (Zero Rate) accuracy is 8.4%, discuss the performance (accuracy and confusion matrix) of your classifier. 