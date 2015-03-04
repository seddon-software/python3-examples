from ReadFile import readFile
from BeautifulSoup import BeautifulSoup

doc = readFile("xml/book.xml")
soup =  BeautifulSoup(doc)

# extract fragments
tags = soup.findAll("author")
newSoup = BeautifulSoup(str(tags))
print newSoup.prettify()

1
    


