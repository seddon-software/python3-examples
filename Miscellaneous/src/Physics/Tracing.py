import numpy as np
from math import sqrt, sin, cos, pi
from Forces import *




def inRange(frameRange, frame):
    """range is a 3-tuple of frame values:  (lowerBound, upperBound, step)"""
    lo = frameRange[0]
    hi = frameRange[1]
    step = frameRange[2]
    if(frame < lo): return False
    if(frame > hi): return False
    if(frame % step != 0): return False
    return True
    
def traceElectron(e):
    p = e.position_
    v = e.velocity_
    if(e.number == 0):
        le = e.previousLorentzForce_[1]
    else:
        le = e.previousLorentzForce_[0]
    lp = e.previousLorentzForce_[2]
    print "electron: {0} {1:8.5f}".format(e.number, modulus(e.position_))
    print "       x: {0:8.5f},{1:8.5f},{2:8.5f}".format(p[0], p[1], p[2])
    print "       v: {0:8.5f},{1:8.5f},{2:8.5f}".format(v[0], v[1], v[2])
    print "      le: {0:8.5f},{1:8.5f},{2:8.5f}".format(le[0], le[1], le[2])
    print "      lp: {0:8.5f},{1:8.5f},{2:8.5f}".format(lp[0], lp[1], lp[2])

def traceElectricForceBetweenTwoParticles(frameRange, frame, particles, particle1number, particle2number):
    if(not inRange(frameRange, frame)): return
    particle1 = None
    particle2 = None
    for particle in particles:
        if(particle.number == particle1number): particle1 = particle
        if(particle.number == particle2number): particle2 = particle
    if(particle1 == None or particle2 == None): raise Exception("Invalid particle numbers in <traceElectricForceBetweenTwoParticles>")
    field_ = electricField(particle1, particle2, period)
    separation = modulus(particle1.position_ - particle2.position_)
    print "Frame {0}: Electric Field {1}->{2}:({3:8.2f})".format(frame, particle1number, particle2number, separation),
    print "Frame {0}: Electric Field {1}->{2}:".format(frame, particle1number, particle2number),
    print "{0:8.4f},{1:8.4f},{2:8.4f}".format(field_[0], field_[1], field_[2])

def traceMagneticForceBetweenTwoParticles(frameRange, frame, particles, particle1number, particle2number):
    if(not inRange(frameRange, frame)): return
    particle1 = None
    particle2 = None
    for particle in particles:
        if(particle.number == particle1number): particle1 = particle
        if(particle.number == particle2number): particle2 = particle
    if(particle1 == None or particle2 == None): raise Exception("Invalid particle numbers in <traceElectricForceBetweenTwoParticles>")
    field_ = electricField(particle1, particle2, period)
    print "Frame {0}: Electric Field {1}->{2}:".format(frame, particle1number, particle2number),
    print "{0:8.4f},{1:8.4f},{2:8.4f}".format(field_[0], field_[1], field_[2])

    

def debugIt(title, e, p, v_):
    pass
#    print title + ": {0},{1}:{2:8.5f},{3:8.5f},{4:8.5f}".format(e.number, p.number, v_[0], v_[1], v_[2])

def traceParticleRadii(frameRange, frame, particles):
    if(not inRange(frameRange, frame)): return
    print "Frame {0}:".format(frame),
    for particle in particles:
        r = modulus(particle.position_)
        print "{0:6.2f}".format(r),
    print
