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

def proton2electron(t, period, dz = 0.02):
    # dz should be small (0 to 0.5)
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

# def electron2proton(t, period):
# # This function is mainly zero, but has a small peak near each period
# # e.g. t = 132, period=50
# #   z = (132 + 25) % 50 - 25 = 7 - 25 = -18
# #   result is non-zero iff -dh < z < +dh
# #   dh has to be fairly small, about period/50
# #   k must be in the range: perod * period * 0.1 < k <  period * period * 1.5
#     k = period * period
#     z = (t  + period / 2) % period - period / 2
#     dh = 1.0
#     upper = dh
#     lower = - dh
#     if z < upper and z > lower:
#         result = -k * cos(z * pi / 2) / (t * t)
#     else:
#         result = 0
#     # note charge is NOT taken into account by this function
#     return result

def electron2electron(t, period, dz = 0.4):
    # dz should be small (0 to 0.5)
    dz = dz * period
    k = period * period
    z = (t  + period / 2) % period - period / 2  # ranges between -period/2 to +period/2
    upper = dz 
    lower = -dz
    if t < period / 2:
        result = k / (t * t)
        result = -k * cos(0.5 * z * pi / dz) / (t * t)
    elif z < upper and z > lower:
        result = 0
    else:
        result = k / (t * t)
    return result

def particle2particle(t, period, firstCharge, secondCharge, dz = 0.02):
    # dz should be small ~ 0.02 (0 to 0.5)
    dz = dz * period
    k = period * period
    z = (t  + period / 2) % period - period / 2  # ranges between -period/2 to +period/2
    upper = dz 
    lower = -dz
    if z < upper and z > lower:
        result = firstCharge * secondCharge * k * cos(0.5 * z * pi / dz) / (t * t)
    else:
        result = 0
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
                
def electricForce(particle1, particle2):
    x1_ = particle1.position_
    x2_ = particle2.position_
    x_ = x1_ - x2_
    x = modulus(x_)
    xHat_ = x_ / x
#     if particle2.charge > 0:
#         force_ = proton2electron(x, period) * xHat_ * particle2.charge
#     else:
#         force_ = electron2electron(x, period, 0.49) * xHat_
    force2_ = particle2particle(x, period, particle1.charge, particle2.charge) * xHat_
    return force2_

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

def lorentzForce2(particle1, particle2):
    x_ = particle1.position_ - particle2.position_
    x = modulus(x_)
    v_ = particle1.velocity_ - particle2.velocity_
    xHat_ = x_ / x
    zHat_ = np.array([0.0, 0.0, 0.1])
    force2 = magneticForce2(x, period, particle1.charge, particle2.charge)
    force2_ = np.cross(v_, zHat_) * force2
    return force2_

def magneticForce(t, period, charge1, charge2, dz = 0.02):
    dz = dz * period
    k = period * period
    z = t % period 
    upper = period/2 + dz 
    lower = period/2 - dz
    if z < upper and z > lower:
        result = charge1 * charge2 * k * sin(0.5 * z * pi / dz) / (t * t)
    else:
        result = 0
    return result

def magneticForce2(t, period, charge1, charge2, dz = 0.02):
    dz = dz * period
    k = period * period
    z = (t  + period / 2) % period - period / 2  # ranges between -period/2 to +period/2
    upper = +dz 
    lower = -dz
    if z < upper and z > lower:
        result = charge1 * charge2 * k * cos(0.5 * z * pi / dz) / (t * t)
    else:
        result = 0
    return result


def printV(v_):
    print " [{0:8.4f},{1:8.4f},{2:8.4f}] ".format(v_[0], v_[1], v_[2]),

def determinePathsOfElectrons(proton, *electrons):
    # electron-electon interations
    for e1 in electrons:
        dv_ = np.array([0.0, 0.0, 0.0])
        for e2 in electrons:
            if id(e1) != id(e2):
                dve_ = electricForce(e1, e2)
                dv_ = dv_ + dve_
        e1.velocity_ = e1.velocity_ + dv_
    # electron-proton interactions
    for e in electrons:
        dve_ = electricForce(e, proton)
        dve = modulus(dve_)
        dvm_ = lorentzForce2(e, proton)
        dvm = modulus(dvm_)        
        dv_ = dve_ * magicE + dvm_ * magicM
#         printV(dve_)
#         printV(dvm_)
        e.velocity_ = e.velocity_ + dv_
#         printV(e.velocity_)
    for e in electrons:
        e.position_ = e.position_ + e.velocity_ * dt
#         if modulus(e.position_) < 10.0: e.position_ = np.array([9999.0, 0.0, 0.0])
        if modulus(e.position_) < 10.0: raise Exception("Hit proton")
    
def startSimulation(frames):
    p  = Particle('protons',  +3, +0.0, initialPosition_ = [   0.0,  0.0,  0.0], initialVelocity_ = [0.0, 0.0, 0.0])
    e1 = Particle('electron', -1, +0.5, initialPosition_ = [  28.0,  0.0,  1.0], initialVelocity_ = [ -v, 0.0, 0.0])
    e2 = Particle('electron', -1, -0.5, initialPosition_ = [ -28.0,  0.0, -1.0], initialVelocity_ = [ +v, 0.0, 0.0])
    e3 = Particle('electron', -1, -0.5, initialPosition_ = [   0.0, 28.0,  0.0], initialVelocity_ = [0.0,  -v, 0.0])

    e = Particle('electron', -1, -0.5, initialPosition_ = [ a, 0.0, 0.0], initialVelocity_ = [-v, 0.0, 0.0])
    for frame in range(frames):
        determinePathsOfElectrons(p, e)
        traceParticleRadii(traceFrames, frame, e)
#         traceDistanceBetweenParticles(e2, e3)
#         traceElectricForceBetweenTwoParticles(frameRange, frame, particles, 1, 0)
#         alertForceBetweenTwoParticles(electricForce, frameRange, frame, particles, 1, 2, 0.001)
        
print 9 * 0.529 ** 3 / 2

frames = 16000
traceFrames = (0, frames, 2000)
v = 0.00001
magicE = 0.01
magicM = 0.02
print "magicE, magicM = {0:8.2f},{1:8.2f}".format(magicE, magicM), 
print "v={0:8.5f}".format(v) 
a = 10.0

for magicE in np.arange(0.01, 0.2, 0.01):
    for magicM in np.arange(0.01, 0.2, 0.01):
        try:
            print "magicE, magicM = {0:8.2f},{1:8.2f}".format(magicE, magicM), 
            print "v={0:8.5f}".format(v), 
            startSimulation(frames)
        except Exception, e:
            print e
