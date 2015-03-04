############################################################
#
#    reshaping arrays
#
############################################################

from numpy import *

# create array
a = ones( (24,) ); print a

# reshape it
b = a.reshape(2,3,4); print b

# display properties
print type(b)
print "Shape:", b.shape
print "Dimensions:", b.ndim
print "Size:", b.size
print "Item type:", b.dtype.name
print "Item size:", b.itemsize

1
