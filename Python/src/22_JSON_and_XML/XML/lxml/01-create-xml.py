############################################################
#
#    create-xml.py
#
############################################################


from lxml import etree


def addEntry(root, titleText, authorText, firstName, lastName):
    title = etree.SubElement(root, "title")
    author = etree.SubElement(root, "author")
    title.text = titleText
    author.set("firstName", firstName)
    author.set("lastName", lastName)
    author.text = authorText


book = etree.Element("book")
addEntry(root=book, 
         titleText="The Firm", 
         firstName="John F", 
         lastName="Grisham", 
         authorText="Lawyer, popular writer ...")
addEntry(root=book, 
         titleText="For Your Eyes Only: James Bond 007", 
         firstName="Ian", 
         lastName="Fleming", 
         authorText="author, journalist and naval intelligence officer ...")
#author.text="author, journalist and naval intelligence officer ..."


e = etree.ElementTree(element=book, file=None)
e.write('xml/Book.xml', encoding='UTF-8', xml_declaration=True, pretty_print=True)




    