############################################################
#
#    operating on arrays
#
############################################################

import numpy as np
np.set_printoptions(precision=3)


a = np.array( [3,3,3,3,4,3,3] )
b = np.array( [5,5,5,5,6,5,5] )

# operations are performed on each element
c = a * b + 2
print c

a = np.arange(10)
b = a ** 3
c = a ** 0.5
print b
print c

# dot and cross product
a = np.array( [[ 2,4], [3,5]] )
b = np.array( [[ 0,1], [1,0]] )
c = np.dot(a,b); print c
c = np.cross(a,b); print c
print

# arrays are mutable
a = np.ones( (2,2) )
print a, id(a)
a *= 3
print a, id(a)      # same array
b = a * 3
print a, id(a)
print b, id(b)      # different array

1
