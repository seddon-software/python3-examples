from ReadFile import readFile
from BeautifulSoup import BeautifulSoup

doc = readFile("xml/book.xml")
soup =  BeautifulSoup(''.join(doc))
print soup.prettify()

