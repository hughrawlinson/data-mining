import csv;
import sqlite3;

def knn(d,k,data):
    distancedData = {}
    for record in data:
        distance = compareRecords(d,record)
        distancedData[distance] = record
    print distancedData

def compareRecords(a,b):
    distance = 0;
    for i in range(1,5):
        if a[i] != b[i]:
            distance += 1
    return distance;

if __name__ == "__main__":
    prepareSqliteWithData();
       print knn([11,"Yes","Yes","No","No","Yes",None],3,diagnosesreader)

def prepareSqliteWithData(csvreader):
    conn = sqlite3.connect('example.db')
    with open('diagnoses.csv', 'rb') as diagnoses:
        diagnosesreader = csv.reader(diagnoses, delimiter=',',quotechar='|')
    header = csvreader.next();


