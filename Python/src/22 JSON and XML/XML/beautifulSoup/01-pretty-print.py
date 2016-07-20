from ReadFile import readFile
from bs4 import BeautifulSoup

doc = readFile("xml/book.xml")
soup =  BeautifulSoup(''.join(doc), 'lxml')
print(soup.prettify())

