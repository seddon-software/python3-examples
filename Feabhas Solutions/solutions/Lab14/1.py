#!/usr/bin/env python

import os

mydirname = os.getcwd()
mydir = os.listdir('.')

print "Directory: {}".format(mydirname)
for file in mydir:
    print file
    
