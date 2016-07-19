import sys
import re
import mechanize
import webbrowser
import os
from BeautifulSoup import BeautifulSoup, Tag


def correctURL(url):
    # add the bbc website to URL if it is missing
    base = "http://www.bbc.co.uk"
    old = 'href="/'
    new = 'href="' + base + "/"
    return url.replace(old, new)

# use mechanize to scrape spans from BBC news page
br = mechanize.Browser()
br.open("http://www.bbc.co.uk/news")

response = br.follow_link(text_regex=r"UK")
data = br.response().read()

# pick out anchors that are tagged with the story class
soup = BeautifulSoup(data)
# tags = soup.findAll("a", "story")
tags = soup.findAll("a")
newSoup = BeautifulSoup()

base = "http://www.bbc.co.uk"
for tag in tags:
    # add base url if it is missing from href
    if tag[u'href'][0] == "/": tag[u'href'] = base + tag[u'href']
    # add tag to new soup followed by a <br>  
    newSoup.insert(0, tag)
    newSoup.insert(0, Tag(soup, "br"))

# convert soup into a string
data = str(newSoup)

# save scraped info to a file
try:
    f = open("out.html", "w")
    f.write(data)
    f.close()
except IOError, e:
    print e

# display local file in browser
try: 
    url = "file:///" + os.getcwd().replace("\\", '/') + "/out.html"
    webbrowser.open_new_tab(url)    
except Exception, e:
    print e
    

1
