# Supervised Machine Learning with Python: Text Classification #

Naive Bayes is an simple and efficient classification algorithm that is based on the Bayes theorem that can be formulated as ($c$ is a class, and $W$ a lexical feature):

$$P(c|t) = \frac{P(t|c) P(c)}{P(t)}$$

With the Bayes theorem, we can compute the probability of a class (e.g., virgo in the horroscopes data) given a lexical feature (e.g., 'stressed'). $P(t|c)$ is the probablity (or likelihood) of the lexical feature given that the class is true. $P(c)$ and $P(t)$ are the independent probabilities of the class and lexical feature in a given data set. So for the horroscopes data set, the Bayes theorem can be applied as


$$P(virgo|\text{`stressed'}) = \frac{P(\text{`stressed'}|) P(virgo)}{P(\text{`stressed'})}$$

and we call

| component | label |
|:-:|---|
| $P(c \mid t)$ | Posterior Probability |
| $P(t \mid c)$ | Likelihood |
| $P(c)$ | Prior Probability |
| $P(t)$ | Marginal Likelihood |

## Naive Bayes Algorithm ##

1. Compute posterior probability for target class using the Bayes rule
2. Compute posterior probability for alternative class(-es) using the Bayes rule
3. Compare posteriors and choose class based on maximum posterior probability

And moving to document classification, the probability of a document $d$ being in class $c$, $P(c \mid d)$ is computed as:

$$P(c \mid d) \propto P(c) \prod_{i = 1}^{m}P(t_i \mid c) $$

and the class of a document $d$ is then computed as:

$$c_{MAP} = arg~max_{c \in \{c_1, c_2 \}} P(c \mid d)$$

## Spam or Ham: Implementing a Naive Bayes spam filter with `scikit-learn` ##

First we need multiple components for our pipeline from `scikit-learn`, which is probably the most useful and robust library for traditional machine learning in Python. It provides a selection of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction via a consistence interface in Python.

```py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
```

We start by reading and deduplicating data. _Deduplication_ refers to any technique for eliminating a dataset's redundant data (i.e., removing exacts copies).

```py
data = pd.read_csv(args['dataset'])
print(f'[INFO] number of documents: {data.shape[0]}')
data.drop_duplicates(inplace=True)
print(f'[INFO] number of documents after dedublication: {data.shape[0]}')    
```

Which results is ~0.6 % data reducation

```sh
[INFO] number of documents: 5728
[INFO] number of documents after dedublication: 5695
```

Extract a corpus of email texts and vectorize using raw word counts

```py
corpus = data['text']
cv = CountVectorizer()
```

Extract model data and split 80/20 training/testing data set. The train-test split procedure is used to estimate the performance of machine learning algorithms when they are used to make predictions on data not used to train the model.

It is a fast and easy procedure to perform, the results of which allow you to compare the performance of machine learning algorithms for your predictive modeling problem. Although simple to use and interpret, there are times when the procedure should not be used, such as when you have a small dataset and situations where additional configuration is required, such as when it is used for classification and the dataset is not balanced.

```py
X = cv.fit_transform(corpus.values).toarray()
y = data.iloc[:, 1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)
```

Instantiate and call (_train_) the Naive Bayes classifier. In this example we use a multinomial Naive Bayes algorithm. The multinomial Naive Bayes algorithm is a probabilistic learning method that is mostly used for NLP tasks. The algorithm is based on the Bayes theorem and predicts the tag of a text such as a piece of email or newspaper article. It calculates the probability of each tag for a given sample and then gives the tag with the highest probability as output.

```py
classifier = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
classifier.fit(X_train , y_train)
```

Compute classification matrix. A confusion matrix (aka. error matrix) is a summary of prediction results on a classification problem. The number of correct and incorrect predictions are summarized with count values and broken down by each class.

```py
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
``` 

```sh
[[859   9]
 [  3 268]]
```

Compute the classification accuracy (relative and absolute). Classification accuracy is a metric that summarizes the performance of a classification model as the number of correct predictions divided by the total number of predictions.

```py
print(f'Relative Accuracy; {accuracy_score(y_test, y_pred)}')
print(f'Accuracy in instances {accuracy_score(y_test, y_pred, normalize=False)}')
```

```sh
Relative Accuracy; 0.9894644424934153
Correctly classified instances 1127
```

Run (10-fold) cross validation (CV) and report the distribution of accuracy. Cross validation generally refers to _k_-fold cross validation. In _k_-fold cross validation you have multiple(k) train-test sets instead of 1. This basically means that in a k-fold CV you will be training your model _k_-times and also testing it _k_-times.

```py
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)    
print(accuracies.mean())
print(accuracies.std())
```
Compare 1-fold to 10-fold performance

```sh
0.9892447464815886
0.004221630540517682
```

Plot the distribution of accuracies from your CV.


```py
plt.hist(accuracies, density=True, bins=30)  # density=False would make counts
plt.xlabel('Accuracy')
plt.ylabel('Probability')
plt.xlabel('Data')
plt.savefig('figs/nb_acc_dist.png')
plt.close()
```
