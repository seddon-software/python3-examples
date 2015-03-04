############################################################
#
#    dom-like-parsing.py
#
############################################################

# parse entire XML file from a file
from lxml import etree


doc = etree.parse('xml/book.xml')
print(etree.tostring(doc, pretty_print=True))

1
