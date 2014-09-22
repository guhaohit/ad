import csv
from numpy import *

def labeledit(i):
	reader = csv.reader(open("Downloads/train.csv"))
	alllabel = []
	featurec1 = set([])
	trainad = []

	for line in reader:
		trainad.append(line[i+15])
	#	trainad[0].append(line[15])

	featurec1 = set(trainad)
	for j in range(len(trainad)):
		labelprint = []
		labelprint.append(list(featurec1).index(trainad[j]))
		#trainad[j] = list(featurec1).index(trainad[j])
		alllabel.append(labelprint)
		print(j)

	csvfile = file('feature'+str(i)+'.scv', 'wb')
	writer = csv.writer(csvfile)

	writer.writerows(alllabel)

	csvfile.close()
	return 0

def haha():
	return 5