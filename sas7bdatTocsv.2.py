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


        (options,args) = parser.parse_args()
        for file in ([options.sasFile]):
                if not (file):
                        parser.print_help()
                        sys.exit(0)

        sasFile = options.sasFile
	with SAS7BDAT(sasFile) as f:
    		for row in f:
			line = str(row[0])
			for i in range(1,len(row)):
				row[i] = str(row[i])
				row[i] = row[i].replace(",", ";")
				line += ", %s" % (str(row[i]))
			print line


if __name__ == '__main__':
        main()








