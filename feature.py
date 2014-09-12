import csv
from numpy import *

def labeledit():
	reader = csv.reader(open("Downloads/train.csv"))
	labelfeature = []
	alllabel = []
	for i in range(26):
		featurec1 = set([])
		trainad = []
		for line in reader:
			trainad.append(line[i+15])
		featurec1 = set(trainad)
		for j in range(len(trainad)):
			trainad[j] = list(featurec1).index(trainad[j])
			print(j)
		labelfeature.append(trainad)
		print(i)
	labelmat = mat(labelfeature)
	alllabel = list(labelmat.T)

	csvfile = file('label_feature.csv', 'wb')
	writer = csv.writer(csvfile)

	writer.writerows(alllabel)

	csvfile.close()
	return 0

def haha():
	return 3