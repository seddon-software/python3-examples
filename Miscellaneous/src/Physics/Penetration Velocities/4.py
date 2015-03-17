import numpy as np
from pylab import sqrt, trapz, pi, cos, sin, plt

def modulus(x_):
    return sqrt(x_.dot(x_))


def particle2particle(t, period, dz = 0.02):
    # charge = 1 for like charges and -1 for unlike charges
    # dz should be small ~ 0.02 (0 to 0.5)
    dz = dz * period
    k = period * period
    z = (t  + period / 2) % period - period / 2  # ranges between -period/2 to +period/2
    upper = dz 
    lower = -dz
    if z < upper and z > lower:
        result = -k * cos(0.5 * z * pi / dz) / (t * t)
    else:
        result = 0
    return result

def electricField(x_, period):
    x = modulus(x_)
    xHat_ = x_ / x
    force_ = particle2particle(x, period) * xHat_
    return force_

def lorentzForce(x_, v_, previousForce_, period):
    k = period * period
    x = modulus(x_)
    zeta = sin(x * pi / period)
    v = modulus(v_)
    delta = 0.000001
    if v < delta: 
        return np.array([0.0, 0.0, 0.0])
    vHat_ = v_ / v
    zHat_ = np.array([0.0, 0.0, 1.0])
    force_ =  np.cross(zHat_, vHat_) * zeta * zeta * k * v / (x * x)
    return force_

period = 50

x_ = np.array([60.0, 0.0, 0.0])
v_ = np.array([-0.1, 0.0, 0.0])
dt = 1
previousForce_ = np.array([0.0, 0.0, 0.0])        

# for frame in range(500):
#     print "{0}:".format(frame),
#     print "{0:8.4f}:{1:8.4f}".format(x_[0], v_[0])
#     force_ = electricField(x_, period)
#     dv_ = force_ * dt
#     v_ = v_ + dv_
#     x_ = x_ + v_ * dt
    
for frame in range(500):
    print "{0}:".format(frame),
    print " [{0:8.4f},{1:8.4f},{2:8.4f}] ".format(x_[0], x_[1], x_[2]),
    print " [{0:8.4f},{1:8.4f},{2:8.4f}] ".format(v_[0], v_[1], v_[2])
    force_ = lorentzForce(x_, v_, previousForce_, period)
    previousForce_= force_
    dv_ = (force_ - previousForce_) * dt
    v_ = v_ + dv_
    x_ = x_ + v_ * dt
