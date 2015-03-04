############################################################
#
#    faster-sax-like-parsing.py
#
############################################################

# stream document through parser
from lxml import etree


infile = "xml/Book.xml"
outfile = "text/authors2.txt"

# iterparse only looks at a subset of nodes
context = etree.iterparse(infile, 
                          events=('end',), 
                          tag='author')
out = open(outfile, 'w')
for event, elem in context:
    out.write('%s\n' % elem.text.encode('utf-8'))

out.close()



1


    