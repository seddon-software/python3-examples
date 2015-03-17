from scipy import integrate
import numpy as np
#from pylab import *
#from scipy.integrate import quad
from pylab import sqrt, trapz, pi, cos, sin, plt
from _imaging import path

def modulus(x_):
    return sqrt(x_.dot(x_))

"""
function to integrate at various points
"""
def func(x_):
    k = 2
    e1_ = np.array([+1.0, 0.0, 0.0])
    e2_ = np.array([-1.0, 0.0, 0.0])
    
    x = modulus(x_)
    x1 = modulus(x_ - e1_)
    x2 = modulus(x_ - e2_)
    f = 2 / (x * x)
    f1 = -1 / (x1 * x1)
    f2 = -1 / (x2 * x2)
    force = k * (f + f1 + f2)
    return force 

def radius(x_):
    return modulus(x_)

""" 
compute a series of equally spaced points from start_ to stop_ with increment inc
"""
def points(start_, stop_, number):
    xd = [x for x in np.linspace(start_[0], stop_[0], number)]
    yd = [y for y in np.linspace(start_[1], stop_[1], number)]
    path = [ np.array([xy[0], xy[1], 0.0]) for xy in zip(xd, yd) ]
    return path

start_ = np.array([10.0, 0.0, 0.0])
stop_ = np.array([2.0, 0.0, 0.0])
 
path = points(start_, stop_, 1000)
y = [func(z) for z in path]
x = [radius(p) for p in path]
# integrate func along path defined by path
print "*********", trapz(y, x)

angle = [ ]
v = []
for theta in np.arange(0, pi/2, 0.1):
    r0 = 10.0
    r1 = 2.0
    start_ = np.array([r0 * cos(theta), r0 * sin(theta), 0.0])
    stop_ = np.array([r1 * cos(theta), r1 * sin(theta), 0.0])
    path = points(start_, stop_, 10000)
    y = [func(p) for p in path]
    x = [radius(p) for p in path]
    angle.append(theta)
    v.append(trapz(y, x))
    

fig = plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
fig.set_size_inches(15.5, 11.5)
ax = fig.add_subplot(1, 1, 1)
# x = y = np.arange(-3.0, 3.0, 0.05)
# X, Y = np.meshgrid(x, y)
# zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
# Z = zs.reshape(X.shape)
# 
# ax.plot_surface(X, Y, Z)

import matplotlib.pyplot as plt
print v
redCircles = "ro"
plt.plot(angle, v, redCircles)
plt.xlabel("angle")
plt.ylabel("v")
plt.show()


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')

plt.show()
