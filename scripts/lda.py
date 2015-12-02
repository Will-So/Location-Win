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


def generate_corpus(df, grouper='name', text='text', save=False):
    """
    Generates a dictionary with stopwords and most frequent words removed.
    Also tells how many items have been removed. Optionally allows saving the
    files to disk.

    :param df: pd.DataFrame()
    :param grouper: The column that we want to group by. For example, by restaurant.
    :param text: The column with the text that we want to model by
    :param save: boolean that
    :return: corpus, and dict object.

    Example
    ----
    >>> corpus, dictionary = generate_corpus(df, save=True) # doctest: +SKIP
    """
    # Combine the text on a restaurant level
    grouped_df = df.groupby(grouper)
    all_review_text = grouped_df[text].apply(lambda x: '\n'.join(x)).reset_index()

    # Do some Processing
    all_review_text[text] = all_review_text[text].apply(
        lambda x: gensim.utils.simple_preprocess(x))

    # Generate the dictionary
    dictionary = generate_dictionary(all_review_text[text])

    # Generate the corpus
    corpus = [dictionary.doc2bow(t) for t in all_review_text[text]]

    if save:
        try:
            gensim.corpora.MmCorpus.serialize('../data/deerwester.mm', corpus)
            dictionary.save('../data/words.dict')
        except IOError as e:
            logging.warning("Could not save to disk. Exception {}".format(e))

    return corpus, dictionary


def generate_dictionary(series):
    """
    Generates a gensim dictionary.

    :param series: pd.Series. Usually a column of a dataframe
    :return:
    """
    dictionary = gensim.corpora.Dictionary(series)
    original_dict_length = len(dictionary)

    stopwords = set(nltk.corpus.stopwords.words('english'))
    stopwords_ids = list(map(dictionary.token2id.get, stopwords))
    dictionary.filter_tokens(stopwords_ids)
    dictionary.filter_extremes(no_below=10, no_above=0.1)

    dictionary.compactify()
    percent_removed = 1 - (len(dictionary) / original_dict_length)
    logging.info('Removed {} items from our dictionary. {} %'
                 .format(original_dict_length - len(dictionary),
                         percent_removed))

    return dictionary
