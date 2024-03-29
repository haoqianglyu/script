import os,sys
import string
import json
from optparse import OptionParser
import csv
from Bio import SeqIO


__version__="1.0"
__status__ = "Dev"



"""
This script has three options, you can execute the script in three ways:

1. python dump-fasta-stats.py --version
This is the option that show you the program's version.

2. python dump-fasta-stats.py -h
This can show you some help information.

3. python dump-fasta-stats.py -i xxx.fasta
This will check the .fasta file that if there are duplicate IDs in the sequence. 
If yes, it will output "Id repeated: bad fasta file".
If no, it will output the number of sequence.

"""


###############################
def main():

	usage = "\n%prog  [options]"
	parser = OptionParser(usage,version="%prog " + __version__)
	parser.add_option("-i","--infile",action="store",dest="infile",help="FASTA input file")


	(options,args) = parser.parse_args()
	for file in ([options.infile]):
		if not (file):
			parser.print_help()
			sys.exit(0)


	inFile = options.infile
	seen = {}
	count = 0
	for record in SeqIO.parse(inFile, "fasta"):
		if record.id in seen:
			print ("Id repeated: bad fasta file")
			sys.exit()
		count += 1
		seen[record.id] = True

	print ("Number of sequence:", count)




if __name__ == '__main__':
        main()


