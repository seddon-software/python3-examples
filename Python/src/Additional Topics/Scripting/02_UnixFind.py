############################################################
#
#    search directory tree
#
############################################################

import os, re

# search for all files with .egg extension
for root, dirs, files in os.walk('C:\python26'):
    for name in files:
        # note use of os.sep
        if re.search("[.]egg$", name) != None: 
            print root + os.sep + name
1
