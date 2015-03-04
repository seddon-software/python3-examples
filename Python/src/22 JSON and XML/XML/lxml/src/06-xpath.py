############################################################
#
#    xpath.py
#
############################################################

from lxml import etree


try:
    doc = etree.parse('xml/Book.xml')
    fragment = doc.xpath("//author[2]")
    print(etree.tostring(fragment[0], pretty_print=True, encoding='iso-8859-1'))
except Exception, reason:
    print reason


1


    