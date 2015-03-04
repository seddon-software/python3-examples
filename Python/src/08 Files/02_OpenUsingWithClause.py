############################################################
#
#    Using with
#
############################################################

from __future__ import with_statement # not required in Python 2.6

# successful read
try:
    with open("data/hello.txt", "r") as f:
        for line in f:
            print line,
except IOError,e:
    print e

# unsuccessful read
try:
    with open("data/unknown-file.txt", "r") as f:
        for line in f:
            print line,
except IOError,e:
    print e


