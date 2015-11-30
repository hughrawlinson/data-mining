"""Utility functions for a KNN implementation"""
from hashlib import md5


# Doesn't get used, was for keying a cache
def getMd5(arg):
    """
    Takes arbitrary data, returns an md5 hash
    """
    x = md5()
    x.update(arg)
    return x.digest()


def histogram(data):
    """Generates a histogram for arbitrary data"""
    hist = {}
    for index, value in enumerate(data):
        try:
            hist[value] += 1
        except Exception:
            hist[value] = 1
    return hist


def arrayToReverseDict(array):
    """
    Swaps keys and values from a list, in the process converting it into
    a dict
    """
    d = {}
    for index, value in enumerate(array):
        d[value] = index
    return d
