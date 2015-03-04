############################################################
#
#    xpath.py
#
############################################################

import webbrowser
import os
from lxml import etree

stylesheet = "xml/Sorting.xsl"
xmlfile = "xml/Names.xml"

stylesheet_doc = etree.parse(stylesheet)
transformer = etree.XSLT(stylesheet_doc)
xml_doc = etree.parse(xmlfile)

result_tree = transformer(xml_doc)

# save to a file
try:
    f = open("out.html", "w")
    f.write(str(result_tree))
    f.close()
except IOError, e:
    print e
    
# display local file in browser
try: 
    url = "file:///" + os.getcwd().replace("\\", '/') + "/out.html"
    webbrowser.open_new_tab(url)    
except Exception, e:
    print e

1


    