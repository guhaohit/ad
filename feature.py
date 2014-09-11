import csv

def labeledit():
	reader = csv.reader(open("Downloads/train.csv"))
	trainad = []
	featurelen = []
	for i in range(26):
		featurec1 = set([])
		for line in reader:
			trainad.append(line[i+15])
		featurec1 = set(trainad)
		featurelen.append(len(featurec1))
	return featurelen

def haha():
	return 2