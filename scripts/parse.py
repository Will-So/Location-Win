"""
Copied from my previous project

Loads yelp data into a Pandas Dataframe.


"""

import pandas as pd
import sys
import logging

DATA_DIR = '/Users/Will/Data/newest_yelp/'

HDF = False
GENERATE_SAMPLE = False
GENERATE_RESTAURANT_REVIEWS = True


def _main():
    """
    Generates the business and reviews dataframes from the YELP JSON format and
    converts it to a pd.DataFrame. Optionally will also save a sample to it to an
    HDF file.

    """
    reviews = reviews_to_pandas(DATA_DIR)
    businesses = businesses_to_pandas(DATA_DIR)

    if HDF:
        print("Writing to hdf")
        reviews.to_hdf('../data/reviews.hdf', 'df', mode='w', format='f')
        businesses.to_hdf('../data/businesses.hdf', 'businesses', mode='w', format='f')

    if GENERATE_SAMPLE:
        sample_reviews = reviews.sample(frac=0.1)
        sample_businesses = businesses.sample(frac=0.1)
        sample_businesses.to_hdf('../data/sample_sample_businesses.hdf', 'df', mode='w', format='f')
        sample_reviews.to_hdf('../data/sample_reviews.hdf', 'businesses', mode='w', format='f')

    if GENERATE_RESTAURANT_REVIEWS:
        restaurants = find_restaurants(businesses)
        restaurant_reviews = reviews.merge(restaurants, how='inner', on='business_id')
        restaurant_reviews = clean_rest_reviews(restaurant_reviews)

        restaurant_reviews.to_hdf('../data/restaurant_reviews.hdf', 'df', mode='w', format='f')
        restaurant_reviews.sample(frac=0.1).to_hdf('../data/sample_rest_reviews.hdf', 'df',
                                                    mode='w', format='f')




def reviews_to_pandas(dir):
    """

    Parameters
    ----------
    dir

    Returns
    -------

    Examples
    ----
    >>> df = reviews_to_pandas(DATA_DIR)
    >>> df.head(2)

    """

    data = load_json_file(dir + 'yelp_academic_dataset_review.json')
    df = parse_large_df(data)

    return df


def businesses_to_pandas(dir):
    """
    Loads JSON and returns a dataframe
    """
    data = load_json_file(dir + 'yelp_academic_dataset_business.json')
    df = parse_large_df(data)
    df = df.drop('attributes', axis=1)

    return df


def parse_large_df(data, normalize=False):
    """
    Hacky way to deal with dataframes that are large quickly from a json file.

    Parameters
    ----------
    data: A list of the json objects

    Returns
    -------
    df: dataframe
    """
    minis = {}
    for i in range(1, (len(data)), 10000):
        j = i + 10000
        data_json_str = "[" + ','.join(data[i:j]) + "]"
        temp = pd.read_json(data_json_str)
        minis[i] = temp
        print(str(j) + ' rows in a df')

        df = pd.DataFrame()
    for i in range(1, (len(data)), 10000):
        df = pd.concat([df, minis[i]], ignore_index=True, axis=0)
        print('appending {}'.format(i))

    return df


def load_json_file(json_dir):
    """
    Loads a json file with the directory

    Returns
    -------
    A list of JSON objects.

    """
    with open(json_dir) as jsonfile:
        data = jsonfile.readlines()
        # remove the trailing "\n" from each line
        data = list(map(lambda x: x.rstrip(), data))

    return data


def join_businesses_reviews(reviews, businesses):
    """

    Parameters
    ----------
    reviews
    businesses

    Returns
    -------

    """
    df = reviews.join(businesses, on='review_id', how='inner')
    del df['stars_y']
    print("Lost {} Reviews during the join process".format(len(reviews) - len(df)))


    return df


def find_restaurants(df):
    """
    Constructs a

    Parameters
    ----------
    df


    """
    df['is_rest'] = False
    # TODO: use Apply for this instead of iterrows
    for i, val in df.iterrows():
        if 'Restaurants' in val.categories:
            df.loc[i, 'is_rest'] = True

    restaurants = df[df.is_rest == True]

    return restaurants


def clean_rest_reviews(df):
    """
    Removes unneccesary features and renames a column
    """
    df = df.rename(columns={'stars_x': 'stars'})
    df = df[['date', 'review_id', 'text', 'user_id',
                   'city', 'latitude', 'longitude', 'name', 'neighborhoods',
                   'stars', 'hours']]
    return df



if __name__ == '__main__':
    sys.exit(_main())
