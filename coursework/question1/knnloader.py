"""A """
import csv
import numpy as np


def getDataFromFilename(filename):
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


def writeResultsToDisk(header, results, data, filename):
    """
    Takes a path to a file, saves data to file.

    Named Keywords
    filename -- a string containing the file path
    """
    for i, datum in enumerate(data):
        np.append(data, results[i])
    header.append("diagnosis")
    np.insert(data, 0, header)
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            writer.writerow(row)
    return header, np.array(data)
