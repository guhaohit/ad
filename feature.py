import csv
from numpy import *

def labeledit():
	reader = csv.reader(open("Downloads/train.csv"))
	trainad = []
	labelfeature = []
	for i in range(26):
		featurec1 = set([])
		for line in reader:
			trainad.append(line[i+15])
		featurec1 = set(trainad)
		for j in range(len(trainad)):
			trainad[j] = list(featurec1).index(trainad[j])
		labelfeature.append(trainad)
	labelarray = array(labelfeature)
	labelfeature = list(labelarray.T)
	csvfile = file('label_feature.csv', 'wb')
	writer = csv.writer(csvfile)

	writer.writerows(labelfeature)

	csvfile.close()

def haha():
	return 3