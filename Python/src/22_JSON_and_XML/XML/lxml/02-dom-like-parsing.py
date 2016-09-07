############################################################
#
#    dom-like-parsing.py
#
############################################################

# parse entire XML file from a file
from lxml import etree
doc = etree.parse('xml/book.xml')
encoding = doc.docinfo.encoding
s = etree.tostring(doc, xml_declaration=True, encoding=encoding, pretty_print=True)
print( s.decode('UTF-8') )


