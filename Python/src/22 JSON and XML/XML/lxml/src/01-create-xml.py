############################################################
#
#    create-xml.py
#
############################################################


from lxml import etree

xmlDeclaration = etree.ProcessingInstruction(
            target="xml", 
            text="version='1.0' encoding='UTF-8' standalone='no'")

book = etree.Element("book")
book.addprevious(xmlDeclaration)
title = etree.SubElement(book, "title")
author = etree.SubElement(book, "author")
publisher = etree.SubElement(book, "publisher")

title.text = "The Firm"
author.set("firstName", "John F")
author.set("lastName", "Grisham")
author.text="Lawyer, popular writer ..."

location = etree.SubElement(publisher, "location")
location.text = "UK"
publisher.text = "The Random House"
location.tail = "London, SW1V 2SA"
print(etree.tostring(
            book, 
            pretty_print=True, 
            encoding="UTF-8",
            xml_declaration=True))

xmlText = etree.tostring(
            book, 
            pretty_print=True,
            encoding="UTF-8", 
            xml_declaration=True)

out = open('xml/Book.xml', 'w')
out.write(xmlText)
out.close()

1


    