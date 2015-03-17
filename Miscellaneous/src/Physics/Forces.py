import numpy as np
from math import sqrt, sin, cos, pi

period = 50

def modulus(x):
    return sqrt(x.dot(x))

def func(t, period):
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
    return result

def func2(t, period):
# This function is derived from func and is approximately the opposite of this function
    k = period * period
    z = (t  + period / 2) % period - period / 2
    dh = 1.0
    upper = dh
    lower = - dh
    if z < upper and z > lower:
        result = 0
    else:
        result = -k * cos(z * pi / 2) / (t * t)
    return result

def func2a(t, period):
# This function is derived from func and is approximately the opposite of this function
    k = period * period
    z = (t  + period / 2) % period - period / 2
    dh = 1.0
    upper = dh
    lower = - dh
    if z < upper and z > lower:
        result = -k * cos(z * pi / 2) / (t * t)
    else:
        result = -k * cos(z * pi / 2) / (t * t)
    return result

def determineSpin(i):
    return 1
#    return - ((i%2) * 2 - 1)

def electricFieldx(particle1, particle2, period):
    x1_ = particle1.position_
    x2_ = particle2.position_
    x_ = x1_ - x2_
    x = modulus(x_)
    xHat_ = x_ / x
    if particle2.charge > 0:
        force = func(x, period) * xHat_
    else:
        force = func2(x, period) * xHat_ / (period)
    return force


def lorentzForcex(particle1, particle2, period):
    x1_ = particle1.position_
    x2_ = particle2.position_
    x_ = x1_ - x2_
    v1_ = particle1.velocity_
    v2_ = particle2.velocity_
    v_= v1_ - v2_
    
    previousForce_ = particle1.previousLorentzForce_[particle2.number]
    k = period * period
    x = modulus(x_)
    zeta = sin(x * pi / period)
    v = modulus(v_)
    delta = 0.000001
    if v < delta: 
        print "low velocity"
        return np.array([0.0, 0.0, 0.0])
    vHat_ = v_ / v
    zHat_ = np.array([0.0, 0.0, 1.0])
    force_ =  np.cross(zHat_, vHat_) * zeta * zeta * k * v / (x * x)
    particle1.previousLorentzForce_[particle2.number] = force_
    df_ = force_ - previousForce_
    return df_
