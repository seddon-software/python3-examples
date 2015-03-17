import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt, sin, cos, pi
import copy

def update_plot(frame, data, sc, ax, messages, arrow):
    frame = frame
    soa = np.array( [arrow[frame]] )
    X,Y,Z,U,V,W = zip(*soa)
    sc._offsets3d = data[frame]
    ax.set_xlabel(str(frame) + ' X: ' + messages[frame])
    ax.quiver(X,Y,Z,U,V,W, length=100)
    return sc, ax

X = 0
Y = 1
Z = 2
period = 50


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
    

def setupPlot(messages, magneticArrow, frames, scale, data):
    fig = plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
    fig.set_size_inches(16,12)
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
    ani = FuncAnimation(fig, update_plot, frames=frames, fargs=(data, sc, ax, messages, magneticArrow), interval=100, blit=True)
    plt.show()

def modulus(x):
    return sqrt(x.dot(x))

##########################################################################################
#
#    Physical stuff below
#
##########################################################################################

def determinePathOfProton(data, frames, particleNumber):
    for frame in range(frames):
        data[frame][X][particleNumber] = 0.0
        data[frame][Y][particleNumber] = 0.0
        data[frame][Z][particleNumber] = 0.0
    return data

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
            
def initializeParticles(particles):
    numberOfElectrons = len(particles) - 1
    protonNumber = len(particles) - 1
    
    particles[0].charge = -1
    particles[0].number = 0
    particles[0].position_ = np.array([1.0, 0.0, 0.0]) * period
    particles[0].velocity_ = np.array([0.0, 10.0, 0.0]) / period
    particles[protonNumber].charge = numberOfElectrons
    particles[protonNumber].number = numberOfElectrons    # after all electrons
    particles[protonNumber].position_ = np.array([0.0, 0.0, 0.0])
    particles[protonNumber].velocity_ = np.array([0.0, 0.0, 0.0])
    particles[protonNumber].previousLorentzForce_ = None

def lorentzForce(particle1, particle2, period):
    x1_ = particle1.position_
    x2_ = particle2.position_
    x_ = x1_ - x2_
    v1_ = particle1.velocity_
    v2_ = particle2.velocity_
    v_= v1_ - v2_
    
    k = period * period / 10
    x = modulus(x_)
    v = modulus(v_)
    delta = 0.000001
    if v < delta: 
        print "low velocity"
        return np.array([0.0, 0.0, 0.0])
    vHat_ = v_ / v
    zHat_ = np.array([0.0, 0.0, 1.0])
    force_ =  np.cross(zHat_, vHat_) * k * v / (x * x)
    return force_

def determinePathsOfElectrons(particles, protonNumber, dt, magic):
    electrons = copy.copy(particles)    # must be a shallow copy
    electrons.pop();
    
    for e in electrons:
        r = modulus(e.position_)
        if r < 10: raise Exception("hit origin")
        dv_ = np.array([0.0, 0.0, 0.0])
        for p in particles:
            if id(e) != id(p):
                if p.number == protonNumber: 
                    lf_ = lorentzForce(e, p, period)
                dv_ = dv_ + lf_ / dt
                e.velocity_ = e.velocity_ + dv_
        e.position_ = e.position_ + e.velocity_ * dt
        
def writeInfo(messages, magneticArrow, frame, particles):
    x_ = particles[0].position_
    v_ = particles[0].velocity_
    x = modulus(x_)
    v = modulus(v_)
    messages[frame] = "x={0:8.2f},v={1:8.2f}".format(x,v)
    magneticArrow[frame] = [ x_[0],x_[1],x_[2],v_[0],v_[1],v_[2] ]
    
def CreateParticles(numberOfParticles):
    particles = [ ]
    for i in range(numberOfParticles):
        particles.append(Particle(numberOfParticles))
    return particles

def startSimulation(frames, data, numberOfElectrons, messages, magneticArrow, iterationsPerFrame, dt, period):
    particles = CreateParticles(numberOfElectrons + 1)
    protonNumber = numberOfElectrons
    initializeParticles(particles)
    for frame in range(frames):
        print "Frame {0}: ".format(frame),
        for iteration in range(iterationsPerFrame):
            determinePathsOfElectrons(particles, protonNumber, dt, magic=1)
            writeInfo(messages, magneticArrow, frame, particles)
        for particle in particles:
            r = modulus(particle.position_)
            print "{0:4.2f}".format(r),
            data[frame][X][particle.number] = particle.position_[0]
            data[frame][Y][particle.number] = particle.position_[1]
            data[frame][Z][particle.number] = particle.position_[2]
        print
    return data
    
def main():
    scale = 100
    period = 50
    numberOfElectrons = 1
    particles = numberOfElectrons + 1
    dt = 1
    frames = 2000
    iterationsPerFrame = 1
    dimensions = 3
    messages = [None]*frames
    magneticArrow = [None]*frames
    data = np.zeros(frames * dimensions * particles, dtype=float)
    data = data.reshape(frames, dimensions, particles)
    data = startSimulation(frames, data, numberOfElectrons, messages, magneticArrow, iterationsPerFrame, dt, period)
#    data = addParticleTrail(data, frames, electron, electronTrail)
    setupPlot(messages, magneticArrow, frames, scale, data)
    

main()
