import os,sys
import string
from optparse import OptionParser
from lxml import etree
from StringIO import StringIO

__version__="1.0"
__status__ = "Dev"


###############################
def main():

        usage = "\n%prog  [options]"
        parser = OptionParser(usage,version="%prog " + __version__)
        parser.add_option("-i","--xmlFile",action="store",dest="xmlFile",help="Input xml file")

        (options,args) = parser.parse_args()
        for file in ([options.xmlFile]):
                if not (file):
                        parser.print_help()
                        sys.exit(0)

        xmlFile = options.xmlFile

	FR = open(xmlFile)
	xml = FR.read()
        FR.close()

	context =  etree.iterparse(StringIO(xml), events=("start", "end"))
	 
	for action, elem in context:
		if action == "start":
                        if elem.tag == "book":
                                print elem.attrib["id"]
			elif elem.tag == "title":
                                print elem.text





if __name__ == '__main__':
        main()








