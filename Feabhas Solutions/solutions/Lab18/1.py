#!/usr/bin/env python

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
            
        
response = urllib2.urlopen('http://www.feabhas.com')
html = response.read()

parser = UberParser()
parser.feed(html)

print "Num <h1> Tags: {}".format(parser.tags['h1'])
print "Num <h2> Tags: {}".format(parser.tags['h2'])
print "Num <h3> Tags: {}".format(parser.tags['h3'])
