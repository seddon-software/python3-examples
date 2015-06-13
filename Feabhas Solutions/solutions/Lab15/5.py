#!/usr/bin/env python

import sys

ERR_FILE_NOT_EXIST = 1

filename = "does_not_exist.txt"

try:
    fh = open(filename,  'r')
except Exception as ex:
    print str(ex)
    print "{} does not exist".format(filename)
    sys.exit(ERR_FILE_NOT_EXIST)
    
contents = fh.readlines()
fh.close()

try:
    assert (len(contents ) == 2)
except AssertionError as ex:
    # Warn the user
    print "File is not the expected size"
    # Non-fatal error, so allow it to contine
    
for line in contents:
    print line

