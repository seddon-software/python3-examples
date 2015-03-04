from ReadFile import readFile
from BeautifulSoup import BeautifulSoup

doc = readFile("xml/book.xml")
soup =  BeautifulSoup(doc)

tags = soup.findAll("author")  # list of tags

# 3 ways to print tags
for tag in tags:    print str(tag)
for tag in tags:    print tag.renderContents()
for tag in tags:    print tag.prettify()

1
    


