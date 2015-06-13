#!/usr/bin/env python

import os
import sys

for dirname in sys.stdin.readlines():
    # Need to strip off the new line
    dirname = dirname[:-1]
    dirlist = os.listdir(dirname)
    print dirname
    for f in dirlist:
        print f
    # Print a blank line between listings
    print ''
