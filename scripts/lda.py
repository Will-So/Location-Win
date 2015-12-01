"""
Topic modeling. Finds latent topics that may be


Methodology
---



Notes
---
- Need to download stopwords in NLTK

"""
import gensim
import pandas as pd
import nltk
import logging

SAVE = False


def generate_corpus(df, grouper='name', text='text'):
    """
    Generates a dictionary with stopwords and most frequent words removed.
    Also tells how many items have been removed.

    :param df:
    :return:
    """
    # Combine the text on a restaurant level
    grouped_df = df.groupby(grouper)
    all_review_text = grouped_df[text].apply(lambda x: '\n'.join(x)).reset_index()

    # Do some Processing
    all_review_text[text] = all_review_text[text].apply(
        lambda x: gensim.utils.simple_preprocess(x))

    dictionary = gensim.corpora.Dictionary(all_review_text[text])
    original_dict_length = len(dictionary)

    stopwords = set(nltk.corpus.stopwords.words('english'))
    stopwords_ids = list(map(dictionary.token2id.get, stopwords))
    dictionary.filter_tokens(stopwords_ids)
    dictionary.filter_extremes(no_below=10, no_above=0.1)

    dictionary.compactify()
    percent_removed = 1 - (len(dictionary) / original_dict_length)
    logging.log('Removed {} items from our dictionary. {} %'
                .format(original_dict_length - len(dictionary)),
                percent_removed)

    # Generate the corpus
    corpus = [dictionary.doc2bow(t) for t in df[text]]

    if SAVE:
        gensim.corpora.MmCorpus.serialize('../data/deerwester.mm', corpus)
        dictionary.save('../data/words.dict')