############################################################
#
#    creating arrays
#
############################################################

from numpy import *


set_printoptions(precision=3)

# create array filled with 1's
a = ones( (3,5) ); print a
b = ones( (3,5) ) * 13; print b

# create array filled with 0's
a = zeros( (3,5) ); print a

# create empty array
a = empty( (3,5), dtype=int); print a 

# create array from a list
a = array( [2,3,5,7,11,13,17] ); print a
a = array( [ [3,4],[5,6] ]); print a

# create array with random values
a = array( random.random((2,3)) ); print a

# create using arange
a = arange(4);      print a
a = arange(4,17);   print a
a = arange(4,17,3); print a

# create equally spaced arrays
a = linspace(-50.0,50.0,5); print a
a = linspace(-50.0,50.0,7); print a

# use a function
a = fromfunction(lambda i,j: i * j, (3,3))
print a
a = fromfunction(lambda i,j,k: i + j + k, (4,2,3))
print a

1
