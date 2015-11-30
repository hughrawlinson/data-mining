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
