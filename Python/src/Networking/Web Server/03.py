import urllib2
import json
import csv

def getRows(data):
    # ?? this totally depends on what's in your data
    return []

url = "http://localhost:18080/xxx?x=1&y=2&z=3"
data = urllib2.urlopen(url).read()
data = json.loads(data)


print data


