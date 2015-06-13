############################################################
#
#    operating on arrays
#
############################################################

from numpy import *
set_printoptions(precision=3)


a = array( [3,3,3,3,4,3,3] )
b = array( [5,5,5,5,6,5,5] )

# operations are performed on each element
c = a * b + 2
print c

a = arange(10)
b = a ** 3
c = a ** 0.5
print b
print c

# dot and cross product
a = array( [[ 2,4], [3,5]] )
b = array( [[ 0,1], [1,0]] )
c = dot(a,b); print c
c = cross(a,b); print c
print

# arrays are mutable
a = ones( (2,2) )
print a, id(a)
a *= 3
print a, id(a)      # same array
b = a * 3
print a, id(a)
print b, id(b)      # different array

1
