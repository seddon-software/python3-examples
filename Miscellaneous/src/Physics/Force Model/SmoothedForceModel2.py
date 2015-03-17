import pylab as p
import numpy as np
from math import exp, sin, cos, pi


def electricForce(t, period, charge = -1, dz = 0.02):
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

def lorentzForce(particle1, particle2):
    x_ = particle1.position_ - particle2.position_
    v_ = particle1.velocity_ - particle2.velocity_
    try:
        previousForce_ = particle1.previousLorentzForce_[id(particle2)]
    except:
        previousForce_ = np.array([0.0, 0.0, 0.0])        
        particle1.previousLorentzForce_[id(particle2)] = previousForce_
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
    particle1.previousLorentzForce_[id(particle2)] = force_
    df_ = force_ - previousForce_ 
    return df_

def magneticForce(t, period, charge = -1, dz = 0.02):
    dz = dz * period
    k = period * period
    z = t % period 
    upper = period/2 + dz 
    lower = period/2 - dz
    if z < upper and z > lower:
        result = charge * k * sin(0.5 * z * pi / dz) / (t * t)
    else:
        result = 0
    return result

 
max = 250
x = np.arange(0.001, max, 0.01)
ax = p.axis([0, max, -2, 2 ])

y1 = [electricForce(t, 50, dz=0.1)  for t in x]
y2 = [-magneticForce(t, 50, dz=0.1)  for t in x]
p.plot(x,y1, color='red', lw=2)
p.plot(x,y2, color='blue', lw=2)


p.show()

