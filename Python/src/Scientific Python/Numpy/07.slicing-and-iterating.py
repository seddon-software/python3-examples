############################################################
#
#    slicing and iterating
#
############################################################

import numpy as np

# one dimensional arrays
a = np.arange(20); print a
print a[7:14]
print a[2:14:3]
print a[::]
print

# multi-dimensional arrays
a = np.arange(24).reshape(4,3,2); print a
print a[0:2,0:2,0:2]

# iterate (works on first dimension)
print "iteration"
for eachRow in a:
    print eachRow
    
# flatten array (not a function) to iterate over every element
for element in a.flat:
    print element,
print

# Fortran arrays     -> first dimension varies fastest
# C arrays (default) -> last dimension varies fastest 
a = np.arange(24).reshape( (4,3,2), order="C" ) 
for element in a.flat:
    print element,
print

a = np.arange(24).reshape( (4,3,2), order="F" ) # create Fortran array
for element in a.flat:
    print element,
print


