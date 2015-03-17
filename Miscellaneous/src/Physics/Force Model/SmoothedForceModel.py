import pylab as p
import numpy as np
from math import exp, sin, cos, pi

""" this works """
def electron2proton(t, period):
# This function is mainly zero, but has a small peak near each period
# e.g. t = 132, period=50
#   z = (132 + 25) % 50 - 25 = 7 - 25 = -18
#   result is non-zero iff -dh < z < +dh
#   dh has to be fairly small, about period/50
#   k must be in the range: perod * period * 0.1 < k <  period * period * 1.5
    k = period * period
    z = (t  + period / 2) % period - period / 2
    dh = 1.0
    upper = dh
    lower = - dh
    if z < upper and z > lower:
        result = -k * cos(z * pi / 2) / (t * t)
    else:
        result = 0
    # note charge is NOT taken into account by this function
    return result

""" this doesn't work"""
def proton2electronZ(t, period):
    z = 0
    h = t / period
    for n in range(0, 9):
        s = t - n * period
        z = z + exp(-1.8*s*s) / (h * h)
    return z


def electron2electron(t, period, dz = 0.1):
    return particle2particle(t, period, 1, dz)

def proton2electron(t, period, dz = 0.1):
    return particle2particle(t, period, -1, dz)

def particle2particle(t, period, charge, dz = 0.02):
    # charge = 1 for like charges and -1 for unlike charges
    # dz should be small ~ 0.02 (0 to 0.5)
    dz = dz * period
    k = period * period
    z = (t  + period / 2) % period - period / 2  # ranges between -period/2 to +period/2
    upper = dz 
    lower = -dz
    if z < upper and z > lower:
        result = charge * k * cos(0.5 * z * pi / dz) / (t * t)
    else:
        result = 0
    return result

 
max = 50
x = np.arange(0.001, max, 0.01)
ax = p.axis([0, max, -2, 2 ])

y1 = [proton2electron(t, 10, 0.1)  for t in x]
y3 = [electron2proton(t, 50)  for t in x]
y4 = [proton2electron(t, 10, 0.1)  for t in x]
y6 = [electron2electron(t, 10, 0.1)  for t in x]
# p.plot(x,y1, color='red', lw=2)
# p.plot(x,y2, color='blue', lw=2)
# p.plot(x,y3, color='green', lw=2)
p.plot(x,y4, color='blue', lw=2)
p.plot(x,y6, color='red', lw=2)
# p.plot(x,y7, color='red', lw=2)

""" plot difference between f and proton2electron """
diff = [proton2electron(t, 50, 0.2) - electron2electron(t, 50, 0.2)  for t in x]
# p.plot(x,diff, color='green', lw=2)

p.show()

