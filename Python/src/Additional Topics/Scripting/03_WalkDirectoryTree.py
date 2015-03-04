############################################################
#
#    walk directory tree
#
############################################################

import os

for root, dirs, files in os.walk('C:\Temp'):
    print root                          # parent directory
    print "\tSubdirectories: ",dirs     # subdirectories
    print "\tFiles", files              # files in parent directory

1
