import csv


with open("/softwares/util/example.csv", 'rb') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in csvreader:
		for j in xrange(0,len(row)):
			print j,row[j]

