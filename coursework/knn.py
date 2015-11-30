#!/usr/bin/env python
"""A module for building K-Nearest-Neighbor"""

from sys import argv
import numpy as np
import csv
from hashlib import md5


def getDataAsMultidimensionalArrayFromFilename(filename):
    """
    Takes a path to a file, performs I/O, returns data as a multidimensional
    array.

    Named Keywords
    filename -- a string containing the file path
    """
    data = []
    header = []
    with open(filename, 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in datareader:
            if(len(header) < 1):
                header = row
            else:
                data.append(row)
    return header, np.array(data)


def getMd5(arg):
    """
    Takes arbitrary data, returns an md5 hash
    """
    x = md5()
    x.update(arg)
    return x.digest()


def distanceBetweenTwoInstances(instanceA, instanceB):
    """
    Calculates the distance between two rows of our dataset
    """
    distance = 0
    if(instanceA.size == instanceB.size):
        for i in range(0, instanceA.size):
            if(instanceA[i] != instanceB[i]):
                distance += 1
        return distance
    else:
        print "Malformed Data"
        exit(1)


def buildDistances(data, query):
    """
    Builds distances describing the distances between our
    query and each of the rows in the dataset
    """
    distances = np.array([])
    for i in data:
        distance = distanceBetweenTwoInstances(i, query)
        distances = np.append(distances, distance)
    return distances


def getNearestNeighbours(distanceRow, k):
    """
    Takes a row of distances, returns the indices of the
    lowest k values
    """
    return np.argpartition(distanceRow, -k)[-k:]


def getFeaturesFromNearestNeighbours(neighbourIndices, dataset, featureIndex):
    """
    Takes a list of row numbers, returns the set of their values
    for a particular column in each row of our dataset.
    """
    features = []
    for index in neighbourIndices:
        features.append(dataset[index][featureIndex])
    return features


def arrayToReverseDict(array):
    """
    Swaps keys and values from a list, in the process converting it into
    a dict
    """
    d = {}
    for index, value in enumerate(array):
        d[value] = index
    return d


def vote(features):
    """
    Takes a list of features, returns the most common feature of the list.
    """
    hist = histogram(features)
    return sorted(hist, key=hist.get)[-1]


def main(arg):
    results = []
    k = int(arg[1])
    dataFilePath = arg[2]
    testDataFilePath = arg[3]
    searchKey = arg[4]
    header, data = getDataAsMultidimensionalArrayFromFilename(dataFilePath)
    _, testData = getDataAsMultidimensionalArrayFromFilename(testDataFilePath)
    for queryRow in testData:
        result = knn(
            k,
            searchKey,
            queryRow,
            header,
            data
        )
        results.append(result)
    print histogram(results)


def knn(k, searchKey, queryRow, header, data):
    headerIndices = arrayToReverseDict(header)
    distances = buildDistances(data, queryRow)
    neighbourIndices = getNearestNeighbours(distances, k)
    features = getFeaturesFromNearestNeighbours(
        neighbourIndices,
        data,
        headerIndices[searchKey])
    return vote(features)


def histogram(data):
    """Generates a histogram for arbitrary data"""
    hist = {}
    for index, value in enumerate(data):
        try:
            hist[value] += 1
        except Exception:
            hist[value] = 1
    return hist


if __name__ == '__main__':
    main(argv)
