#!/usr/bin/env python

import urllib2
import HTMLParser 
import argparse
import sys

ERR_URL = 1

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
            
        

parser = argparse.ArgumentParser()

parser.add_argument("url", help="URL to fetch", type=str)
parser.add_argument("-t", "--tags",  help="Depth of headers to display", type=int)

args = parser.parse_args()


try:
    response = urllib2.urlopen(args.url)
except ValueError as ex:
    print str(ex)
    sys.exit(ERR_URL)
    
html = response.read()

parser = UberParser()
parser.feed(html)

for depth in range(1, args.tags+1):
    tag= "h{}".format(depth)
    print "Num <{}> Tags: {}".format(tag,  parser.tags[tag])
