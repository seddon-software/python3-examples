from ReadFile import readFile
from bs4 import BeautifulSoup

doc = readFile("xml/book.xml")
soup =  BeautifulSoup(doc, 'lxml')

# extract fragments
tags = soup.findAll("author")
newSoup = BeautifulSoup(str(tags))
print(newSoup.prettify())

1
    


