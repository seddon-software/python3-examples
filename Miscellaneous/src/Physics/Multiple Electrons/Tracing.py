import numpy as np
from math import sqrt, sin, cos, pi

def modulus(x):
    return sqrt(x.dot(x))

def inRange(traceRange, frame):
    """range is a 3-tuple of frame values:  (lowerBound, upperBound, step)"""
    lo = traceRange[0]
    hi = traceRange[1]
    step = traceRange[2]
    if(frame < lo): return False
    if(frame > hi): return False
    if(frame % step != 0): return False
    return True

def traceNonZeroElectricField(dve_, dvm_, traceFrames, frame):
    if(not inRange(traceFrames, frame)): return
    if modulus(dve_) < 0.000001:
        print "dve,dvm : {0:8.5f}{1:8.5f}".format(modulus(dve_), modulus(dvm_)),
        print "dvm_: {0:8.5f},{1:8.5f},{2:8.5f}".format(dvm_[0], dvm_[1], dvm_[2])

def traceZeroElectricField(dve_, dvm_, traceFrames, frame):
    if(not inRange(traceFrames, frame)): return
    if modulus(dve_) >= 0.000001:
        print "dve,dvm : {0:8.5f}{1:8.5f}".format(modulus(dve_), modulus(dvm_)),
        print "dvm_    : {0:8.5f},{1:8.5f},{2:8.5f}".format(dvm_[0], dvm_[1], dvm_[2])

def traceDistanceBetweenParticles(p1, p2):
    r = modulus(p1.position_ - p2.position_)
    print "separation: {0:8.2f}".format(r)

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

def alertForceBetweenTwoParticles(func, traceRange, frame, particles, particle1number, particle2number, threshold):
    if(not inRange(traceRange, frame)): return
    particle1 = None
    particle2 = None
    for particle in particles:
        if(particle.number == particle1number): particle1 = particle
        if(particle.number == particle2number): particle2 = particle
    if(particle1 == None or particle2 == None): raise Exception("Invalid particle numbers in <traceElectricForceBetweenTwoParticles>")
    field_ = func(particle1, particle2, period)
    if modulus(field_) > threshold:
        separation = modulus(particle1.position_ - particle2.position_)
        print "\tFrame {0}: Electric Field {1}->{2}:({3:8.4f})".format(frame, particle1number, particle2number, modulus(field_)),
        print "[{0:8.4f},{1:8.4f},{2:8.4f}]".format(field_[0], field_[1], field_[2])

def traceForceBetweenTwoParticles(func, traceRange, frame, particles, particle1number, particle2number):
    if(not inRange(traceRange, frame)): return
    particle1 = None
    particle2 = None
    for particle in particles:
        if(particle.number == particle1number): particle1 = particle
        if(particle.number == particle2number): particle2 = particle
    if(particle1 == None or particle2 == None): raise Exception("Invalid particle numbers in <traceElectricForceBetweenTwoParticles>")
    field_ = func(particle1, particle2, period)
    separation = modulus(particle1.position_ - particle2.position_)
    print "Frame {0}: Electric Field {1}->{2}:({3:8.2f})".format(frame, particle1number, particle2number, separation),
    print "Frame {0}: Electric Field {1}->{2}:".format(frame, particle1number, particle2number),
    print "{0:8.4f},{1:8.4f},{2:8.4f}".format(field_[0], field_[1], field_[2])

def traceMagneticForceBetweenTwoParticles(traceFrames, frame, particles, particle1number, particle2number):
    if(not inRange(traceFrames, frame)): return
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

def traceParticleRadii(traceFrames, frame, *particles):
    if(not inRange(traceFrames, frame)): return
    print "Frame {0}:".format(frame),
    for particle in particles:
        r = modulus(particle.position_)
        print "{0:6.2f}".format(r),
    print
