############################################################
#
#    array types
#
############################################################

from numpy import *
set_printoptions(precision=3)

# create array of int
a = array( [2,3,5,7,11,13,17] )
print a

# create array of float
a = array( [sqrt(x) for x in 2,3,5,7,11,13,17], dtype="float64" )
print a

# create array of complex
a = array( [x*(1.5+2.0j) for x in 2,3,5,7,11,13,17], dtype="complex64" )
print a


1
