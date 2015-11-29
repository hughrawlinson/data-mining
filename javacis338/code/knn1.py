import csv;

y = Yes = yes = "Yes"
n = No = no = "No"

#Todo: write OrderedDict sort lambda
#Todo: grab the most occurring top diagnosis from three, print it

if __name__ == "__main__":
    query = [11,y,n,y,n,y,None]
    keyedDistances = {}
    with open('diagnoses.csv', 'rb') as diagnoses:
        diagnosesreader = csv.reader(diagnoses, delimiter=',', quotechar='|')
        header = csvreader.next
        for record in data:
            keyedDistances[record[0]] = distance(query,record)
        KNearestNeighbours = OrderedDict(keyedDistances,lambda)[:3]
        

