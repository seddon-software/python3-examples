import sys
import re
import mechanize
import webbrowser
import os
import requests

def correctURLs(url):
    # add the bbc website to URL if it is missing
    base = "http://www.bbc.co.uk"
    old = 'href="/'
    new = 'href="' + base + "/"
    return url.replace(old, new)

# use mechanize to scrape spans from Google Finance page
br = mechanize.Browser()
br.open("http://www.bbc.co.uk/news")
response = br.follow_link(text_regex=r"UK")
data = br.response().read()

# pick out spans that are tagged with class="story"
# pattern = r'(<a class="story".*?</a>)'
pattern = r'(<a.*?</a>)'

pattern = re.compile(pattern, re.S)     # S modifier for multiline support
matcher = re.findall(pattern, data)     # find all the spans as a list

# some spans have the incorrect urls which need the modifying
newMatcher = []
for match in matcher:
    newMatcher.append(correctURLs(match))

# create a string of spans separated by breaks
data = "<br>".join(newMatcher)             

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
