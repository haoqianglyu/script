import os,sys
import string
from optparse import OptionParser
from Bio import SeqIO
import re

__version__="1.0"
__status__ = "Dev"

"""
This script has three options, you can execute the script in three ways:

1. python fastq-parser.py --version
This is the option that show you the program's version.

2. python fastq-parser.py -h
This can show you some help information.

3. python fastq-parser.py -i xxx.fastq
This option will print the read_id, read_seq and read_qual in the fastq file.
"""
###############################
def main():

        usage = "\n%prog  [options]"
        parser = OptionParser(usage,version="%prog " + __version__)
        parser.add_option("-i","--fastqFile",action="store",dest="fastqFile",help="Input fastqFile")

        (options,args) = parser.parse_args()
        for file in ([options.fastqFile]):
                if not (file):
                        parser.print_help()
                        sys.exit(0)

        fastqFile = options.fastqFile

        qual_sum = 0
        n = 0
        c_count, g_count = 0, 0
	for record in SeqIO.parse(fastqFile, "fastq"):
                read_id = record.id
                read_seq = str(record.seq)
                read_qual = record.letter_annotations["phred_quality"]
                print read_id
                print read_seq
                print read_qual
                print "\n"

                #c_count += len(re.findall(r"C",read_seq))
                #g_count += len(re.findall(r"G",read_seq))
                #qual_sum +=  int(read_qual)
                n += 1
        #average = qual_sum/n

        #print "total quality for the first position %s for %s reads" % (qual_sum, n)
        #print "average quality %s " %(average) 
        #print c_count + g_count





if __name__ == '__main__':
        main()








