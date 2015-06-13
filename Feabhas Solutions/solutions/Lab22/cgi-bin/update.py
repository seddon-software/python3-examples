#!/usr/bin/python

import sys
import json
import cgi

import urllib2
import HTMLParser 

class UberParser(HTMLParser.HTMLParser):
    
    def __init__(self):
        # Call the parent's initmethod
        HTMLParser.HTMLParser.__init__(self)
        self.tags = {}
        
    def handle_starttag(self, tag, attrs):
        #print "Encountered a start tag:", tag
        try:
            self.tags[tag] += 1
        except KeyError as ex:
            self.tags[tag] = 1
            
        
form = cgi.FieldStorage()

print "Content-Type: text/plain"     # HTML is following
print                               # blank line, end of headers

site =  form.getfirst('url',  '')
url = "http://"+site
element = form.getfirst('element',  '')

response = urllib2.urlopen(url)
html = response.read()

parser = UberParser()
parser.feed(html)

print json.dumps(parser.tags)
