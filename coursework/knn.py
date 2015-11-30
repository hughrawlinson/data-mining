#!/usr/bin/env python
"""A module for building K-Nearest-Neighbor"""

from sys import argv
import numpy as np
import knnloader
import knnutil as util


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


def vote(features):
    """
    Takes a list of features, returns the most common feature of the list.
    """
    hist = util.histogram(features)
    return sorted(hist, key=hist.get)[-1]


def main(arg):
    results = []
    k = int(arg[1])
    dataFilePath = arg[2]
    testDataFilePath = arg[3]
    searchKey = arg[4]
    header, data = knnloader.getDataFromFilename(dataFilePath)
    _, testData = knnloader.getDataFromFilename(testDataFilePath)
    for queryRow in testData:
        result = knn(
            k,
            searchKey,
            queryRow,
            header,
            data
        )
        results.append(result)
    print util.histogram(results)


def knn(k, searchKey, queryRow, header, data):
    headerIndices = util.arrayToReverseDict(header)
    distances = buildDistances(data, queryRow)
    neighbourIndices = getNearestNeighbours(distances, k)
    features = getFeaturesFromNearestNeighbours(
        neighbourIndices,
        data,
        headerIndices[searchKey])
    return vote(features)





if __name__ == '__main__':
    main(argv)
