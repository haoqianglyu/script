import os,sys
import string
import csv
from optparse import OptionParser
from sas7bdat import SAS7BDAT


__version__="1.0"
__status__ = "Dev"


###############################
def main():

        usage = "\n%prog  [options]"
        parser = OptionParser(usage,version="%prog " + __version__)
        parser.add_option("-i","--sasFile",action="store",dest="sasFile",help="Input sas file")
	parser.add_option("-o","--csvFile",action="store",dest="csvFile",help="Output csv file")


        (options,args) = parser.parse_args()
        for file in ([options.sasFile, options.csvFile]):
                if not (file):
                        parser.print_help()
                        sys.exit(0)

        sasFile = options.sasFile
	outFile = options.csvFile
	FW = csv.writer(open('outFile', 'wb'))
	with SAS7BDAT(sasFile) as f:
    		for row in f:
			FW.writerow(row)



if __name__ == '__main__':
        main()








