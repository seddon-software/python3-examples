#!/usr/bin/env python

import os
import glob

FILENAME = "TestFile"
# cd to TestDirectory
os.chdir('TestDirectory')

mydir = glob.glob('*.txt')
for file in mydir:
    print file
    
