############################################################
#
#    surface plots
#
############################################################

from numpy import *
import Gnuplot
import math
import setup


g = Gnuplot.Gnuplot(debug=1)

# Demonstrate a 3-d plot:
# set up x and y values at which the function will be tabulated:
x = arange(25)
y = arange(25)

# Make a 2-d array containing a function of x and y.  First create
# xm and ym which contain the x and y values in a matrix form that
# can be `broadcast' into a matrix of the appropriate shape:
xm = x[:,newaxis]
ym = y[newaxis,:]
m = xm**2 * ym**2 

g('set parametric')
g('set data style lines')
g('set hidden')
g('set contour base')
g.title('An example of a surface plot')
g.xlabel('x')
g.ylabel('y')

g.splot(Gnuplot.GridData(m,x,y))


1
