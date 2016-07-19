############################################################
#
#    walk directory tree
#
############################################################

import os

for root, dirs, files in os.walk('/tmp'):
    print root                          # parent directory
    print "\tSubdirectories: ",dirs     # subdirectories
    print "\tFiles", files              # files in parent directory

1
