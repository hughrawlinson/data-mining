#!/usr/bin/python

from sys import argv
import numpy as np
import csv
from hashlib import md5
import pickle


distanceMatrices = {}


def getDataAsMultidimensionalArrayFromFilename(filename):
    data = []
    header = []
    with open(filename, 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in datareader:
            if(header == []):
                header = row
            else:
                data.append(row)
    return header, data


def getMd5(arg):
    x = md5()
    x.update(arg)
    return x.digest()


def distanceBetweenTwoInstances(instanceA, instanceB):
    distance = 0
    if(len(instanceA) == len(instanceB)):
        for i in range(0, len(instanceA)):
            if(instanceA[i] != instanceB[i]):
                distance += 1
        return distance
    else:
        syntaxErrorLol


def buildDistanceMatrix(data):
    try:
        return distanceMatrices[getMd5(pickle.dumps(data))]
    except Exception as e:
        distanceMatrix = []
        for i in data:
            distanceRow = []
            for j in data:
                distanceRow.append(distanceBetweenTwoInstances(i, j))
            distanceMatrix.append(i)
        distanceMatrices[getMd5(pickle.dumps(data))] = distanceMatrix
        return distanceMatrix


def getNearestNeighbours(distanceRow, k):
    arr = np.array(distanceRow)
    return np.argpartition(arr, -k)[-k:]


def getFeaturesFromNearestNeighbours(neighbourIndices, dataset, featureIndex):
    features = []
    for index in neighbourIndices:
        features.append(dataset[index][featureIndex])
    return features


def arrayToReverseDict(array):
    d = {}
    for index, value in enumerate(array):
        d[value] = index
    return d


def vote(features):
    hist = dict()
    for index, feature in enumerate(features):
        try:
            hist[feature] += 1
        except Exception as e:
            hist[feature] = 1
    return sorted(hist, key=hist.get)[-1]


def main(arg):
    hist = {}
    k = int(arg[1])
    dataFilePath = arg[2]
    testDataFilePath = arg[3]
    searchKey = arg[4]
    header, data = getDataAsMultidimensionalArrayFromFilename(dataFilePath)
    _, testData = getDataAsMultidimensionalArrayFromFilename(testDataFilePath)
    for index, queryInstance in enumerate(testData):
        features, result = knn(
            k,
            dataFilePath,
            searchKey,
            queryInstance,
            header,
            data)
        try:
            hist[result] += 1
        except Exception as e:
            hist[result] = 1
    print hist


def knn(k, dataFilePath, searchKey, queryInstance, header, data):
    headerIndices = arrayToReverseDict(header)
    distanceMatrix = buildDistanceMatrix(data)
    neighbourIndices = getNearestNeighbours(queryInstance, k)
    features = getFeaturesFromNearestNeighbours(
        neighbourIndices,
        data,
        headerIndices[searchKey])
    return features, vote(features)


if __name__ == '__main__':
    main(argv)
