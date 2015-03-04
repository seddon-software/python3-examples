############################################################
#
#    xpath.py
#
############################################################

from lxml import etree


try:
    doc = etree.parse('../resources/01.html')
    path = "//div[@id='question_1_5' and contains(@span,'Does the patient weigh over 350lbs?')]"
    path = "//div[contains(string(span[2]/text()),'D')]"
    path = "//div[@id='question_1_5' and contains(span[2]/text(),'Does the patient weigh over 350lbs?')]"
    fragment = doc.xpath(path)
    print(etree.tostring(fragment[0], pretty_print=True, encoding='iso-8859-1'))
except Exception, reason:
    print reason


1


    