#!/usr/bin/env python

import os
import subprocess

mydirname = os.getcwd()
output = subprocess.Popen(["ls", "-l", mydirname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print "Directory: {}".format(mydirname)

listing = output.stdout.readlines()
# The first line contains the total size, so skip it
for line in listing[1:]:
    line = line.strip()	# Remove the newlines
    # ls pads out columns with spaces. We need to change this to just one
    # Replace two spaces with 1
    spaces_done = False    
    while (not spaces_done):
        check = line.replace('  ', ' ')
    	if (check == line):  # All spaces are now single
    	    spaces_done = True
    	line = check
    sections = line.split(' ')
    perms = sections[0]
    creation = sections[5]+' '+sections[6]+' '+sections[7]
    name = sections[8]
    
    print "Name: {}\nCreated: {}\nPermissions: {}".format(name, creation, perms)
	    
