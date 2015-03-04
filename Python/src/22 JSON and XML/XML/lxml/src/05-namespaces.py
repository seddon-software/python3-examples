############################################################
#
#    create-xml.py
#
############################################################

from lxml import etree

xmlDeclaration = etree.ProcessingInstruction(
            target="xml", 
            text="version='1.0' encoding='UTF-8' standalone='no'")

po = "http://abc.def.com/purchase-order"
lib = "http://abc.def.com/po-library"

NSMAP = { 
         None  : po,
         "lib" : lib 
        }

po  = "{" + po  + "}"
lib = "{" + lib + "}"

book   = etree.Element(po + "book", nsmap = NSMAP)
author = etree.SubElement(book, po + "author")
id     = etree.SubElement(book, lib + "id")
author.text = "John Grisham"
id.text     = "5610783"

print(etree.tostring(
            book, 
            pretty_print=True, 
            encoding="UTF-8",
            xml_declaration=True))


1


    