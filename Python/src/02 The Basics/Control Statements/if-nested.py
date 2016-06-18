############################################################
#
#    if-compound statements
#
############################################################

from math import sqrt

x = 100

if x > 0:
    print('x is positive')
    print('the square of x is', x * x)
    if x > 10:
	    print('the square root of x is', sqrt(x))
