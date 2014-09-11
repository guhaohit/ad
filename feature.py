import csv

def labelchange():
	reader = csv.reader(open("Downloads/train.csv"))
	trainad = []
	featurelen = []
	featurec1 = set([])
	for i in range(26):
		for line in reader:
			trainad.append(line[i+15])
		featurec1 = set(trainad)
	featurelen.append(len(featurec1))
	return featurelen

def haha():
	return 0