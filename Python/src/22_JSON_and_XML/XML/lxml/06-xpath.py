############################################################
#
#    xpath.py
#
############################################################

from lxml import etree

try:
    doc = etree.parse('xml/Book.xml')
    fragment = doc.xpath("//author[2]")
    out = etree.tostring(fragment[0], 
                         pretty_print=True, 
                         encoding='iso-8859-1')
    print(out.decode('iso-8859-1'))
except Exception as reason:
    print(reason)


1


    