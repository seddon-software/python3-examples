#!/usr/bin/env python


filename = "does_not_exist.txt"

fh = open(filename,  'r')
contents = fh.readlines()
fh.close()

for line in contents:
    print line

