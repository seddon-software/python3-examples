############################################################
#
#    create-xml.py
#
############################################################

from lxml import etree

def validation(schema, xml):
    schemaDoc = etree.parse(schema)
    xmlschema = etree.XMLSchema(schemaDoc)

    xmlDoc = etree.parse(xml)
    
    if xmlschema.validate(xmlDoc):
        print "Validation successful"
    else:
        print "**** Validation unsuccessful ****"
        error = xmlschema.error_log.last_error
        print "File:  " + error.filename
        print "Line:  " + str(error.line)
        print "Error: " + error.message
    
validation('xml/BookSchema.xsd', 'xml/MyBooks.xml')
validation('xml/BookSchema.xsd', 'xml/MyBooks2.xml')

1


    

    