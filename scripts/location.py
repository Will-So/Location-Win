"""
Functions for handling distances

Brute Force Method:
In: New Business Point
    1. Filter the df so that only values from the same city are there
    2. Calculate the distance between all other points (see if geopy does this)
    3.

Out:

Improvements:
1. Use k-d tree structure for efficiently finding the nearest points
    http://stackoverflow.com/questions/21829065/pythonic-way-to-get-closest-point-for-each-point-in-a-data-frame-nearest-neighb
    http://stackoverflow.com/questions/28612773/how-to-speed-up-nearest-search-in-pandas-perhaps-by-vectorizing-code/28613358#28613358
2. Calculate only the distances if they are in the same city (basic if control)


"""
from geopy.distance import vincenty
from scipy.spatial import cKDTree as KDTree


def find_distance(df, r1, r2):
    """
    Finds the distance between two points in miles.

    :param df:
    :param r1:
    :param r2:
    :return:
    """

    loc1 = (df.ix[r1]['latitude'], df.ix[r1]['longitude'])
    loc2 = (df.ix[r2]['latitude'], df.ix[r2]['longitude'])

    return vincenty(loc1, loc2).miles


def row_find_nearest_businesses(df, row, k=5, loc_cols=['latitude', 'longitude']):
    """
    Finds the nearest neighbor of a

    :param row: Row that we are interested in finding the nearest neighbors for
    :param df: pd.DataFrame with loc_cols
    :param k:
    :param loc_cols: List of columns that we are comparing to for nearest neighbors
    :return:

    Example
    ---
    >>> find_nearest_neighbors(businesses, 1)
    """
    tree = KDTree(df[loc_cols])
    distance, indices = tree.query(df[loc_cols], k + 1)
    neighbors = df.ix[indices[row][1:]] # Start at 1 to ignore the current index

    return neighbors


def point_find_nearest_businesses(df, point, k=5, loc_cols=['latitude', 'longitude']):
    """
    Given a point (lat, long)
    :param df:
    :param point:
    :param k:
    :param loc_cols:
    :return:
    """
    tree = KDTree(df[loc_cols])
    distance, indices = tree.query(point, k)
    return df.ix[indices]


def compute_avg_success(businesses):
    """
    Computes the average success of selected businesses
    :param businesses: pd.DataFrame of businesses
    :return: float; average success metric
    """
    return businesses.success_metric.mean()