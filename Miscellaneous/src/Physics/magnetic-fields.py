from pylab import *
from numpy import ma

epsilon = 0.00001
delta = 0.1

def northPole(x,y):
    return 100.0 / sqrt(x*x + (y-delta)*(y-delta) + epsilon)

def southPole(x,y):
    return 100.0 / sqrt(x*x + (y+delta)*(y+delta) + epsilon)
#     return 100.0 / sqrt(x * x + (y - epsilon) * (y - epsilon))   
    
max = 5
X,Y = meshgrid( arange(-max, max + epsilon, 0.5),arange(-max, max + epsilon , 0.5) )
U = [x * (northPole(x,y) - southPole(x,y)) for x in X for y in Y]
V = [y * (northPole(x,y) - southPole(x,y)) for x in X for y in Y]


figure()
Q = quiver(X, Y, U, V)
l,r,b,t = axis()
plt.show()


