import os,sys
import string
from optparse import OptionParser
from Bio import SeqIO

__version__="1.0"
__status__ = "Dev"



###############################
def main():

        usage = "\n%prog  [options]"
        parser = OptionParser(usage,version="%prog " + __version__)
        parser.add_option("-i","--fastaFile",action="store",dest="fastaFile",help="Input fastaFile")

        (options,args) = parser.parse_args()
        for file in ([options.fastaFile]):
                if not (file):
                        parser.print_help()
                        sys.exit(0)

        fastaFile = options.fastaFile

	for record in SeqIO.parse(fastaFile, "fasta"):
		if record.id == "ENST00000357654":
			print "%s" % (record.seq)




if __name__ == '__main__':
        main()







