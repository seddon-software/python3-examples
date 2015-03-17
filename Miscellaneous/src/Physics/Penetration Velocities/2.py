from scipy import integrate
import numpy as np
from pylab import *
from scipy.integrate import quad

def modulus(x_):
    return sqrt(x_.dot(x_))

"""
function to integrate at various points
"""
def func(x_):
    x = modulus(x_)
    return 1 / (x * x)

def radius(x_):
    return modulus(x_)

""" 
compute a series of equally spaced points from start_ to stop_ with increment inc
"""
def points(start_, stop_, inc):
    xd = [x for x in np.arange(start_[0], stop_[0], inc)]
    yd = [y for y in np.arange(start_[1], stop_[0], inc)]
    return [ np.array([xy[0], xy[1], 0.0]) for xy in zip(xd, yd) ]

start_ = np.array([1.0, 1.0, 0.0])
stop_ = np.array([2.0, 2.0, 0.0])

path = points(start_, stop_, 0.0001)
y = [func(z) for z in path]
x = [radius(p) for p in path]
# integrate func along path defined by path
print trapz(y, x)



# check integration gives correct results
def f(r):
    return 1 / (r * r)

# integrate exp(-x) between (1,1) and (2,2)
result = quad(f, sqrt(2), sqrt(8))
print result
# print calculated result: -1/r between sqrt(1*1 + 1*1 = 2) and sqrt(2*2 + 2*2 = 8)
print -1.0/sqrt(8.0) + 1.0/sqrt(2.0) 
