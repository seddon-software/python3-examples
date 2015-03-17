import numpy as np
from math import sqrt, sin, cos, pi

from Tracing import *



def modulus(x):
    return sqrt(x.dot(x))

##########################################################################################
#
#    Physical stuff below
#
##########################################################################################
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

def electron2electron(t, period):
# This function is derived from electron2proton and is approximately the opposite of this function
    k = period * period
    z = (t  + period / 2) % period - period / 2
    dh = 1.0
    upper = dh
    lower = - dh
    if z < upper and z > lower:
        result = 0
    else:
        result = -k * cos(z * pi / 2) / (t * t)
    # note charge is NOT taken into account by this function
    return result

def func2a(t, period):
# This function is derived from electron2proton and is approximately the opposite of this function
    k = period * period
    z = (t  + period / 2) % period - period / 2
    dh = 1.0
    upper = dh
    lower = - dh
    if z < upper and z > lower:
        result = -k * cos(z * pi / 2) / (t * t)
    else:
        result = -k * cos(z * pi / 2) / (t * t)
    # note charge is NOT taken into account by this function
    return result

##########################################################################################
#
#    Particle stuff below
#
##########################################################################################

period = 50
dt = 1.0

class Particle:
    def __init__(self, type, charge, spin, initialPosition_, initialVelocity_):
        self.type = type
        self.charge = charge
        self.spin = spin
        self.position_ = np.array(initialPosition_) * period
        self.velocity_ = np.array(initialVelocity_) * period  
        self.previousLorentzForce_ = {}
                
def electricField(particle1, particle2):
    x1_ = particle1.position_
    x2_ = particle2.position_
    x_ = x1_ - x2_
    x = modulus(x_)
    xHat_ = x_ / x
    if particle2.charge > 0:
        force_ = electron2proton(x, period) * xHat_ * particle2.charge
    else:
        force_ = electron2electron(x, period) * xHat_ * particle2.charge
    return force_

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

def determinePathsOfElectrons(proton, *electrons):
    # proton interactions
    for e in electrons:
        dve_ = electricField(e, proton)
        dvm_ = lorentzForce(e, proton)
        dv_ = dve_ + dvm_ * magic
        e.velocity_ = e.velocity_ + dv_
        e.position_ = e.position_ + e.velocity_ * dt

def startSimulation(frames):
    p  = Particle('protons',  +charge, +0.0, initialPosition_ = [   0.0,  0.0,  0.0], initialVelocity_ = [0.0, 0.0, 0.0])
    e1 = Particle('electron', -1, +0.5, initialPosition_ = [  28.0,  0.0,  1.0], initialVelocity_ = [ -v, 0.0, 0.0])
    e2 = Particle('electron', -1, -0.5, initialPosition_ = [ -28.0,  0.0, -1.0], initialVelocity_ = [ +v, 0.0, 0.0])
    e3 = Particle('electron', -1, -0.5, initialPosition_ = [   0.0, 28.0,  1.0], initialVelocity_ = [0.0,  -v, 0.0])
    for frame in range(frames):
        determinePathsOfElectrons(p, e3)
        traceParticleRadii(traceFrames, frame, e3)
#         traceElectricForceBetweenTwoParticles(frameRange, frame, particles, 1, 0)
#         alertForceBetweenTwoParticles(electricField, frameRange, frame, particles, 1, 2, 0.001)
    
frames = 5000
traceFrames = (frames-1, frames-1, 1)
v0 = 0.00001
v = v0
for charge in np.arange(1, 11, 1):
    for magic in np.arange(1, 20, 1):
        for v in np.arange(v0, charge*v0, v0):
            print "charge={0}".format(charge), 
            print "magic={0:8.2f}".format(magic), 
            print "v={0:8.5f}".format(v), 
            startSimulation(frames)
    