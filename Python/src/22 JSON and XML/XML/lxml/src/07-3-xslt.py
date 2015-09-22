############################################################
#
#    xpath.py
#
############################################################

from lxml import etree
from StringIO import StringIO

# This example shows how to replace part of an xml file (an attribute)

f = StringIO('''\
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:a="http://aaa.bbb.ccc">
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="//a:b/@val">
        <xsl:attribute name="val">
            <xsl:value-of select="200000"/>
        </xsl:attribute>
    </xsl:template>
</xsl:stylesheet>''')

xslt_doc = etree.parse(f)
transform = etree.XSLT(xslt_doc)
f = StringIO("""<z:a xmlns:z="http://aaa.bbb.ccc">
                   <z:b val="43000">This is test data 1</z:b>
                   <z:c>This is test data 2</z:c>
                </z:a>""")
doc = etree.parse(f)
result_tree = transform(doc)

print(etree.tostring(
            result_tree, 
            pretty_print=True, 
            encoding="UTF-8",
            xml_declaration=True))
1


    