"""
Sentiment analysis copied from previous project. Used to make the keywords
"""
import pandas as pd
import matplotlib.pyplot as plt
from string import punctuation
import numpy as np

from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix

# TODO Add code for getting most important features

def _main():
    data = pd.read_hdf('../data/sentiment_data.hdf')



def get_text_and_labels(data):
    """
    Converts the star rating in `data` to either positive, negative, or neutral
    """
    data.loc[data.stars.isin([1,2]), 'target'] = -1
    data.loc[data.stars.isin([4,5]), 'target'] = 1
    data.loc[data.stars.isin([3]), 'target'] = 0
    data = data[['text', 'target']]

    return data


def clean_data(data):
    """
    When doing sentiment analysis, I will keep the stop words here as the
    relative frequency of stopwords may end up being important.
    """
    punctuation = punctuation.remove('!') # ! might be important to detemrine the value
    for p in punctuation:
        data.text = data.text.str.replace(p, '')
    data.text = data.text.str.lower()

    return data


def transform_and_fit(data):
    vect = TfidfVectorizer()
    params = {"tfidf__ngram_range": [(1, 1), (1, 2)],
          "svc__C": [.01, .1, 1, 10, 100]}

    clf = Pipeline([("tfidf", TfidfVectorizer(sublinear_tf=True)),
                    ("svc", LinearSVC())])

    gs = GridSearchCV(clf, params, verbose=2, n_jobs=-1)

    gs.fit(data.text, data.target)
    print(gs.best_estimator_)
    print(gs.best_score_)

    return gs


def plot_confusion_matrix(cm, data, title='Confusion matrix', cmap=plt.cm.Blues):
    """
   Plots the function matrix given a confusion matrix

   Warning: Only works on this specific format of the data
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(data.target.unique()))
    plt.xticks(tick_marks, [-1,0,1], rotation=45)
    plt.yticks(tick_marks, [-1,0,1])
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
