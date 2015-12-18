#!/usr/bin/env python
"""A module for building K-Nearest-Neighbor"""

import numpy as np
import knnloader
import knnutil as util
import argparse


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
        # distance = spatial.distance.cdist(i, query, "matching")
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
    diagnosis = sorted(hist, key=hist.get)[-1]
    return diagnosis

def main(arg):
    k = int(arg.k)
    results = []
    dataFilePath = arg.dataFile
    testDataFilePath = arg.testDataFile
    searchKey = arg.propertyToLearn
    header, data = knnloader.getDataFromFilename(dataFilePath)
    headerIndices = util.arrayToReverseDict(header)
    _, testData = knnloader.getDataFromFilename(testDataFilePath)
    confusionMatrix = np.array([0, 0, 0, 0])
    for queryRow in testData:
        searchIndex = headerIndices[searchKey]
        result = knn(
            k,
            searchIndex,
            queryRow,
            header,
            data
        )
        cfMatrixIndex = 1 if result == "Sick" else 0
        cfMatrixIndex += 2 if queryRow[searchIndex] == "Healthy" else 0
        confusionMatrix[cfMatrixIndex] += 1
        results.append(result)
    knnloader.writeResultsToDisk(header, results, testData, "diagnoses.csv")
    computedHistogram = util.histogram(results)
    confusionMatrix = confusionMatrix.astype(float)
    errorRate = (
        confusionMatrix[2] +
        confusionMatrix[1]
    )/(
        confusionMatrix[0] +
        confusionMatrix[1] +
        confusionMatrix[2] +
        confusionMatrix[3]
    )
    accuracyRate = 1 - errorRate
    sensitivity = confusionMatrix[2]/(confusionMatrix[2]+confusionMatrix[3])
    specificity = confusionMatrix[1]/(confusionMatrix[1]+confusionMatrix[0])
    precision = confusionMatrix[2]/(confusionMatrix[2]+confusionMatrix[0])
    print "Accuracy Rate: ", accuracyRate
    print "Error Rate:", errorRate
    print "Sensitivity: ", sensitivity
    print "Specificity: ", specificity
    print "Precision: ", precision
    print confusionMatrix.reshape(2, 2)
    print computedHistogram


def computed(result):
    return 0 if result == "Sick" else 1


def knn(k, searchIndex, queryRow, header, data):
    distances = buildDistances(data, queryRow)
    neighbourIndices = getNearestNeighbours(distances, k)
    features = getFeaturesFromNearestNeighbours(
        neighbourIndices,
        data,
        searchIndex)
    return vote(features)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for KNN')
    parser.add_argument("k", help="The number of Neighbours to use")
    parser.add_argument("dataFile",
                        help="""
                        The path to a CSV file containing your training data
                        """)
    parser.add_argument("testDataFile",
                        help="""
                        The path to a CSV file containing your test data
                        """)
    parser.add_argument("propertyToLearn",
                        help="""
                        The property that you want to learn
                        """)
    main(parser.parse_args())
