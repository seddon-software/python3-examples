############################################################
#
#    sax-like-parsing.py
#
############################################################

# stream document through parser
from lxml import etree


infile = "xml/Book.xml"
outfile = "text/Book.txt"

class AuthorTarget(object):
    def __init__(self):
        self.text = []
    def start(self, tag, attrib):
        if tag == 'author':
            self.is_author = True
        else:
            self.is_author = False
    def end(self, tag):
        pass
    def data(self, data):
        if self.is_author:
            self.text.append(data.encode('utf-8'))
    def close(self):
        return self.text

parser = etree.XMLParser(target = AuthorTarget())
results = etree.parse(infile, parser)    

# When iterated over, 'results' will contain the output from 
# target parser's close() method

out = open(outfile, 'w')
out.write('\n'.join(results))
out.close()


1


    