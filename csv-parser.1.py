import os,sys
import string
import json
from optparse import OptionParser
import csv

__version__="1.0"
__status__ = "Dev"


###############################
def main():

	usage = "\n%prog  [options]"
	parser = OptionParser(usage,version="%prog " + __version__)
	parser.add_option("-i","--infile",action="store",dest="infile",help="Input file")

	(options,args) = parser.parse_args()
	for file in ([options.infile]):
		if not (file):
			parser.print_help()
			sys.exit(0)

	inFile = options.infile

	with open(inFile, 'r') as FR:
        	dataFrame = csv.reader(FR, delimiter=',', quotechar='"')
        	rowCount = 0
		for row in dataFrame:
			rowCount += 1
			print rowCount, row




if __name__ == '__main__':
        main()


