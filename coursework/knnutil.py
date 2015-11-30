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
