#!/usr/bin/env python

import os
import sys
import glob

rm_list= []
startdir = os.getcwd()
for dirname, dirs, files in os.walk('.'):
    for filename in files:
        # Split the filename to get the extension
        (name,  ext) = filename.split('.')
        if (ext == "txt"):
            
            # Create a fully qualified pathname
            path = "{}/{}/{}".format(startdir,  dirname,  filename)
            rm_list.append(path)

for file in rm_list:
    # Remove the file
    os.unlink(file)
    
