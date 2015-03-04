from BeautifulSoup import BeautifulSoup, Tag, NavigableString


soup =  BeautifulSoup()

tag1 = Tag(soup, "person")
tag2 = Tag(soup, "name", [("first","John"),("last","Smith")])
tag3 = Tag(soup, "location", [("country", "uk")])
soup.insert(0, tag1)
tag1.insert(0, tag2)
tag1.insert(1, tag3)
print soup
text = NavigableString("John Gary Smith")
tag2.insert(0, text)
print soup.prettify()


1
    


