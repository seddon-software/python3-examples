############################################################
#
#    grids
#
############################################################

import numpy as np

x = np.arange(1,11)
y = np.arange(1,11)

# Make a 2-d array containing a function of x and y.  First create
# xm and ym which contain the x and y values in a matrix form that
# can be `broadcast' into a matrix of the appropriate shape:

X = x[:,None]      # newaxis and None are interchangeable
Y = y[np.newaxis,:]
print X
print Y

# generate 2D grid of values
M = X * Y 
print M


1

