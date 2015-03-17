import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt, sin, cos, pi
import copy

from Forces import *
from Tracing import *


def update_plot(frame, data, sc, ax, messages):
    frame = frame + 800
    sc._offsets3d = data[frame]
    ax.set_xlabel(str(frame) + ' X: ' + messages[frame])
    return sc, ax

X = 0
Y = 1
Z = 2


"""
   trailCount determines how many previous frames are included in the trail
"""
def addParticleTrail(data, frames, particleNumber, trailCount):
    for n in range(particleNumber + 1, particleNumber + trailCount):
        for frame in range(frames):
            if frame - particleNumber + 1 >= 0:
                data[frame][0][n] = data[frame - n + particleNumber + 1][0][particleNumber]
                data[frame][1][n] = data[frame - n + particleNumber + 1][1][particleNumber]
                data[frame][2][n] = data[frame - n + particleNumber + 1][2][particleNumber]
    return data

def drawCircles(ax, r0, n):
    for r in range(r0, r0 * n, r0/2):
        x = [ ]
        y = [ ]
        z = [ ]
        theta = np.linspace(-pi, pi, 100)
        for angle in theta:
            x.append( sin(angle) * r )
            y.append( cos(angle) * r )
            z.append( 0.0 )
        ax.plot(x, y, z)
    

def setupPlot(messages, frames, scale, data):
    fig = plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
    fig.set_size_inches(8.5,4.5)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    drawCircles(ax, scale, 5)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    max_ = 5 * scale / 2.0
    ax.set_xlim3d([-max_, max_])
    ax.set_ylim3d([-max_, max_])
    ax.set_zlim3d([-max_, max_])
    ax.set_autoscale_on(False)
    ix, iy, iz = data[0]
    sc = ax.scatter(ix, iy, iz, s=100.0, c='red', marker='o')
    ani = FuncAnimation(fig, update_plot, frames=frames, fargs=(data, sc, ax, messages), interval=100, blit=True)
    plt.show()

def modulus(x):
    return sqrt(x.dot(x))

##########################################################################################
#
#    Physical stuff below
#
##########################################################################################

# def determinePathOfProton(data, frames, particleNumber):
#     for frame in range(frames):
#         data[frame][X][particleNumber] = 0.0
#         data[frame][Y][particleNumber] = 0.0
#         data[frame][Z][particleNumber] = 0.0
#     return data

class Particle:
    def __init__(self, numberOfParticles):
        self.number = 0
        self.charge = 0
        self.spin = 0
        self.position_ = np.array([0.0, 0.0, 0.0])
        self.velocity_ = np.array([0.0, 0.0, 0.0])
        self.previousLorentzForce_ = [ ]
        for i in range(numberOfParticles):
            self.previousLorentzForce_.append(np.array([0.0, 0.0, 0.0]))
            


def determinePathsOfElectrons(particles, protonNumber, dt, magic):
    electrons = copy.copy(particles)    # must be a shallow copy
    electrons.pop();
    
    for e in electrons:
        r = modulus(e.position_)
        dv_ = np.array([0.0, 0.0, 0.0])
        for p in particles:
            if id(e) != id(p):
                dve_ = electricField(e, p, period)
                if p.number == protonNumber: 
                    dvm_ = lorentzForce(e, p, period)
                else:
                    dvm_ = np.array([0.0, 0.0, 0.0])
#                 dv_ = dv_ + (dve_ + dvm_ * e.spin) * 0.5 * magic
                dv_ = dv_ + (dve_ + dvm_)
                e.velocity_ = e.velocity_ + dv_
                if p.number != protonNumber: 
                    x = modulus(e.position_)
                    if x < 10: raise Exception("hit origin")
        e.position_ = e.position_ + e.velocity_ * dt
        
def writeInfo(messages, frame, particles):
    x = modulus(particles[0].position_)
    v = modulus(particles[0].velocity_)
    messages[frame] = "x={0:8.2f},v={1:8.2f}".format(x,v)

def CreateParticles(numberOfParticles):
    particles = [ ]
    for i in range(numberOfParticles):
        particles.append(Particle(numberOfParticles))
    return particles

def electricField(particle1, particle2, period):
    x1_ = particle1.position_
    x2_ = particle2.position_
    x_ = x1_ - x2_
    x = modulus(x_)
    xHat_ = x_ / x
    if particle2.charge > 0:
        force = func(x, period) * xHat_ * particle2.charge
    else:
        force = func2a(x, period) * xHat_
    return force

def lorentzForce(particle1, particle2, period):
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

def initializeParticles(particles):
    numberOfElectrons = len(particles) - 1
    protonNumber = len(particles) - 1
    
    for i in range(numberOfElectrons):     # all the electrons
        particles[i].charge = -1
        particles[i].number = i
        particles[i].spin = determineSpin(i)
        if(i == 0):
            particles[i].position_ = np.array([ 8.0,  0.0, 1.0]) * period
            particles[i].velocity_ = np.array([-0.2, -0.1, 0.0]) / period
        if(i == 1):
            particles[i].position_ = np.array([-8.0, 0.0, -1.0]) * period
            particles[i].velocity_ = np.array([ 0.2, 0.0,  0.0]) / period
#         if(i == 2):
#             particles[i].position_ = np.array([28.0, 0.0, 5.0]) * period
#             particles[i].velocity_ = np.array([-1.0, 0.0, 0.0]) / period
        for j in range(numberOfElectrons+1):    # keep a record of interactions with all other particles
            particles[i].previousLorentzForce_[j] = np.array([0.0, 0.0, 0.0])
    particles[protonNumber].charge = numberOfElectrons
    particles[protonNumber].number = numberOfElectrons    # after all electrons
    particles[protonNumber].position_ = np.array([0.0, 0.0, 0.0])
    particles[protonNumber].velocity_ = np.array([0.0, 0.0, 0.0])
    particles[protonNumber].previousLorentzForce_ = None

def startSimulation(frames, data, numberOfElectrons, messages, iterationsPerFrame, dt, period):
    particles = CreateParticles(numberOfElectrons + 1)
    protonNumber = numberOfElectrons
    initializeParticles(particles)
    for frame in range(frames):
        for iteration in range(iterationsPerFrame):
            determinePathsOfElectrons(particles, protonNumber, dt, magic=1)
            writeInfo(messages, frame, particles)
        for particle in particles:
            r = modulus(particle.position_)
            data[frame][X][particle.number] = particle.position_[0]
            data[frame][Y][particle.number] = particle.position_[1]
            data[frame][Z][particle.number] = particle.position_[2]
        traceParticleRadii(frameRange, frame, particles)
#         traceElectricForceBetweenTwoParticles(frameRange, frame, particles, 1, 0)
#         traceElectricForceBetweenTwoParticles(frameRange, frame, particles, 1, 2)
    return data
    
frames = 5000
frameRange = (2350, 2370, 1)
frameRange = (150, 250, 2)
frameRange = (0, frames - 1, 100)

def main():
    scale = 100
    period = 50
    numberOfElectrons = 2
    particles = numberOfElectrons + 1
    dt = 1.0
    iterationsPerFrame = 1
    dimensions = 3
    messages = [None]*frames
    data = np.zeros(frames * dimensions * particles, dtype=float)
    data = data.reshape(frames, dimensions, particles)
    data = startSimulation(frames, data, numberOfElectrons, messages, iterationsPerFrame, dt, period)
#    data = addParticleTrail(data, frames, electron, electronTrail)
#     setupPlot(messages, frames, scale, data)
    

main()
