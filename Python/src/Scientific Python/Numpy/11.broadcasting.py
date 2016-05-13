############################################################
#
#    broadcasting
#
############################################################

import numpy as np

X = np.arange(1,5)
Y = np.arange(1,5)
print "X and Y are 1D arrays"
print X
print Y

# convert to 2D arrays
X = X[:,None]      # newaxis and None are interchangeable
Y = Y[np.newaxis,:]
print "\nX and Y are now 2D arrays"
print X
print Y

# generate 2D grid of values
print "\nbroadcast X and Y"
M = X * Y 
print M


1

