#!/usr/bin/env python

import pycurl
import urllib
class Body:

    def __init__(self):
        self.contents = ''

    def gotData(self, buffer):
        self.contents = self.contents + buffer


payload = [("arg1", "value1"),  ("arg2",  "value2")]

url = "www.curiola.com/index.py"

curl = pycurl.Curl()
body = Body()
payload = urllib.urlencode(payload)
curl.setopt(curl.URL, url)
curl.setopt(curl.POSTFIELDS, payload)
curl.setopt(curl.WRITEFUNCTION, body.gotData)
curl.perform()
curl.close()

print body.contents
