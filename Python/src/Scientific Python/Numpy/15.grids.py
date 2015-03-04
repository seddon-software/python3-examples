############################################################
#
#    grids
#
############################################################

from numpy import *

x = arange(1,11)
y = arange(1,11)

# Make a 2-d array containing a function of x and y.  First create
# xm and ym which contain the x and y values in a matrix form that
# can be `broadcast' into a matrix of the appropriate shape:

xm = x[:,None]      # newaxis and None are interchangeable
ym = y[newaxis,:]
print xm
print ym

# generate 2D grid of values
m = xm * ym 
print m


1

