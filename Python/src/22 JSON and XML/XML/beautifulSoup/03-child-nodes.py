from ReadFile import readFile
from BeautifulSoup import BeautifulSoup

doc = readFile("xml/book.xml")
soup =  BeautifulSoup(doc)

print "<book> has", len(soup.book), "child nodes"

i = 0
for child in soup.book:
    i = i + 1
    print i, ":", child
1
    


