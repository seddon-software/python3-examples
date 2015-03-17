import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt, sin, cos, pi, exp



def modulus(x):
    return sqrt(x.dot(x))

##########################################################################################
#
#    Physical stuff below
#
##########################################################################################

def func(t, period):
# This function is mainly zero, but has a small peak near each period
# e.g. t = 132, period=50
#   z = (132 + 25) % 50 - 25 = 7 - 25 = -18
#   result is non-zero iff -dh < z < +dh
#   dh has to be fairly small and not vary much from period/50
#   k must be in the range: perod * period * 0.1 < k <  period * period * 1.5
    k = period * period
    z = (t  + period / 2) % period - period / 2
    dh = 1
    upper = dh
    lower = - dh
    if z < upper and z > lower:
        result = -k * cos(z * pi / 2) / (t * t)
    else:
        result = 0  # even a small value makes things unstable
    return result


''' x is position vector '''
def electricField(x, period):
    k = period
    r = modulus(x)
    rHat = x / r
    force =  func(r, period) * rHat
    return force

def lorentzForce(X, v_, period):
    # when electric K = 100
    k = period * period # 10000 # 531 to 8834  = orbit 1, 8835-25800 = orbit 2, 25801-25899 unstable, 25900-30000 = orbit 3
    x = modulus(X)
    zeta = sin(x * pi / period)
    v = modulus(v_)
    delta = 0.000001
    if v < delta: 
        print "low velocity"
        return np.array([0.0, 0.0, 0.0])
    vHat_ = v_ / v
    zHat_ = np.array([0.0, 0.0, 1.0])
    force_ =  np.cross(zHat_, vHat_) * zeta * zeta * k * v / (x * x)
    return force_

def determinePathOfElectron(frames, period, offset = 0.0, k = 1, vx = -0.01):
    # initial position and velocity
    electronPosition_ = np.array([1400.0, offset, 0.0])
    electronVelocity_ = np.array([vx, 0.0, 0.0])
    
    n = numberOfPositions = 4
    m = numberOfElectrons = 2
    position_ = [None] * numberOfPositions
    dvel_ = [None] * numberOfElectrons
    position_[0] = np.array([0.0, 0.0, +1.0]) * period
    position_[1] = np.array([0.0, 0.0, -1.0]) * period
    position_[2] = np.array([0.0, 0.0, +2.0]) * period
    position_[3] = np.array([0.0, 0.0, -2.0]) * period
     
    dvm_ = lorentzForce(electronPosition_, electronVelocity_, period)
    for frame in range(frames):
        dve_ = electricField(electronPosition_, period)
        dvmPrevious_ = dvm_
        dvm_ = lorentzForce(electronPosition_, electronVelocity_, period) * k
        dv_ = np.array([0.0, 0.0, 0.0])
        for i in range(numberOfElectrons):
            dvel_[i] = electricField(electronPosition_ - position_[i], period)
            dv_ = dv_ - dvel_[i]
        dv_ = dv_ + (dve_ + dvm_ - dvmPrevious_) * (numberOfElectrons + 1)
        electronVelocity_ = electronVelocity_ + dv_
        electronPosition_ = electronPosition_ + electronVelocity_
        x = modulus(electronPosition_)
        v = modulus(electronVelocity_)
        if x < 10: raise Exception("hit origin")
        # print "x,v: {0:8.3f} {1:8.3f}".format(x, v)
    print "offset,k,x,vx,v^2: {0:8.3f} {1:8.3f} {2:8.3f} {3:8.3f} {4:8.3f}".format(offset, k, x, vx, v*v)

def main():
    period = 50
    frames = 10000
    offset = 0.0
    k = 1.0
    vx = -0.09
    for vx in np.arange(-0.1, 0.0, 0.01):
        determinePathOfElectron(frames, period, k = k, vx = vx)
    

main()
