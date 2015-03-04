############################################################
#
#    stacking arrays
#
############################################################

from numpy import *

a = ones( (3,5) ); print a
b = zeros( (3,5) ); print b

print "stacking"
h = hstack( (a,b) ); print h
v = vstack( (a,b) ); print v

# create a 1D array
a = r_[10:20, 55, 66, 80:90]; print a

1
