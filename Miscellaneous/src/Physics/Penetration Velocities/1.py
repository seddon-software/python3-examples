############################################################
#
#    integration
#
############################################################

from scipy import * 
from scipy.integrate import quad
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

"""
integration using quadrature
"""
def f(x):
    return exp(-x)

def Force(x):
    return 1 / (x * x)

# for r in np.arange(100, 1, -0.01):
#     result = quad(Force, 100, r)    
#     print "result", r, result[0],
#     print "error estimate", result[1]
    


def modulus(x_):
    return sqrt(x_.dot(x_))

def Force_(x_):
    k = 1
    x = modulus(x_)
    xHat_ = x_ / x
    return k * xHat_ / (x * x)
    
def fun(x_):
    v_ = np.array(np.array([0.0, 0.0, 0.0]))
    v[0] = quad(Force_[0], numpy.inf, args=x_)
    v[1] = quad(Force_[1], numpy.inf, )
    return modulus(v_)

def F_(x_):
    return modulus(x_)

xd = array([0.0,  1.57,  3.14,  4.71,  6.28])
yd = array([0,  2.57,  3.14,  3.71,  6.28])

#fig = plt.figure()
fig = plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
fig.set_size_inches(15.5, 11.5)
ax = fig.add_subplot(1, 1, 1, projection='3d')
#ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-3.0, 3.0, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

1