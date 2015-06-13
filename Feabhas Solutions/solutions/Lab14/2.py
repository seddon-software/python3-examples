#!/usr/bin/env python

import os

FILENAME = "TestFile"
# cd to TestDirectory
os.chdir('TestDirectory')
fd = open(FILENAME)

mydirname = os.getcwd()
mydir = os.listdir('.')
print "Directory: {}".format(mydirname)
for file in mydir:
    print file
    
