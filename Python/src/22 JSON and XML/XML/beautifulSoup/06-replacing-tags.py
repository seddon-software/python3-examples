from ReadFile import readFile
from BeautifulSoup import BeautifulSoup, Tag


doc = readFile("xml/book.xml")
soup =  BeautifulSoup(doc)

# replace all authors
tags = soup.findAll("author")
i = 0
for oldTag in tags:
    i = i + 1
    newTag = Tag(soup, "newTag", [("id", str(i))])
    newTag.insert(0, "text #" + str(i))
    oldTag.replaceWith(newTag)

print soup.prettify()


1
    


