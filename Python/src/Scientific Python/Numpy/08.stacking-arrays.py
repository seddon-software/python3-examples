############################################################
#
#    stacking arrays
#
############################################################

import numpy as np

a = np.ones( (3,5) ); print a
b = np.zeros( (3,5) ); print b

print "stacking"
h = np.hstack( (a,b) ); print h
v = np.vstack( (a,b) ); print v

# create a 1D array
a = np.r_[10:20, 55, 66, 80:90]; print a
# r_ is a class
# r_[...] is translated to r_.getitem(....)
print np.r_
1
