import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt, sin, cos, pi
import copy


def update_plot(frame, data, sc, ax, messages):
    frame = frame + 800
    sc._offsets3d = data[frame]
    ax.set_xlabel(str(frame) + ' X: ' + messages[frame])
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
            
def func(t, period):
# This function is mainly zero, but has a small peak near each period
# e.g. t = 132, period=50
#   z = (132 + 25) % 50 - 25 = 7 - 25 = -18
#   result is non-zero iff -dh < z < +dh
#   dh has to be fairly small, about period/50
#   k must be in the range: perod * period * 0.1 < k <  period * period * 1.5
    k = period * period
    z = (t  + period / 2) % period - period / 2
    dh = 1
    upper = dh
    lower = - dh
    if z < upper and z > lower:
        result = -k * cos(z * pi / 2) / (t * t)
    else:
        result = 0
    return result

def determineSpin(i):
    return 1
#    return - ((i%2) * 2 - 1)

def initializeParticles(particles):
    numberOfElectrons = len(particles) - 1
    protonNumber = len(particles) - 1
    
    for i in range(numberOfElectrons):     # all the electrons
        particles[i].charge = -1
        particles[i].number = i
        particles[i].spin = determineSpin(i)
        if(i == 0):
            particles[i].position_ = np.array([8.0 * period, 0.0, 1 * period])
            particles[i].velocity_ = np.array([-0.5/period, -0.5/period, 0.0])
        if(i == 1):
            particles[i].position_ = np.array([-8.0 * period, 0.0, -1 * period])
            particles[i].velocity_ = np.array([0.5/period, 0.5/period, 0.0])
        if(i == 2):
            particles[i].position_ = np.array([18.0 * period, 18 * period, 0.0])
            particles[i].velocity_ = np.array([-0.01/period, -0.01/period, 0.0])
        for j in range(numberOfElectrons+1):    # keep a record of interactions with all other particles
            particles[i].previousLorentzForce_[j] = np.array([0.0, 0.0, 0.0])
    particles[protonNumber].charge = numberOfElectrons
    particles[protonNumber].number = numberOfElectrons    # after all electrons
    particles[protonNumber].position_ = np.array([0.0, 0.0, 0.0])
    particles[protonNumber].velocity_ = np.array([0.0, 0.0, 0.0])
    particles[protonNumber].previousLorentzForce_ = None


def electricField(particle1, particle2, period):
    x1_ = particle1.position_
    x2_ = particle2.position_
    x_ = x1_ - x2_
    x = modulus(x_)
    xHat_ = x_ / x
    force =  func(x, period) * particle2.charge * xHat_
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

def debugElectron(e):
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

def debugIt(title, e, p, v_):
    pass
#    print title + ": {0},{1}:{2:8.5f},{3:8.5f},{4:8.5f}".format(e.number, p.number, v_[0], v_[1], v_[2])

def determinePathsOfElectrons(particles, protonNumber, dt, magic):
    electrons = copy.copy(particles)    # must be a shallow copy
    electrons.pop();
    
    for e in electrons:
        r = modulus(e.position_)
        dv_ = np.array([0.0, 0.0, 0.0])
        for p in particles:
            numberE = e.number
            numberP = p.number
            if id(e) != id(p):
                dve_ = electricField(e, p, period)
                debugIt("EEEE", e, p, dve_)
                if p.number == protonNumber: 
                    dvm_ = lorentzForce(e, p, period)
                    debugIt("MMMM", e, p, dvm_)
                else:
                    dvm_ = np.array([0.0, 0.0, 0.0])
                dv_ = dv_ + (dve_ + dvm_ * e.spin) * 0.5 * magic
                debugIt("dv  ", e, p, dv_)
                e.velocity_ = e.velocity_ + dv_
                debugIt("v   ", e, p, e.velocity_)
                if p.number != protonNumber: 
                    x = modulus(e.position_)
                    if x < 10: raise Exception("hit origin")
        e.position_ = e.position_ + e.velocity_ * dt
        if(e.number == 3) :debugElectron(e)
        
def writeInfo(messages, frame, particles):
    x = modulus(particles[0].position_)
    v = modulus(particles[0].velocity_)
    messages[frame] = "x={0:8.2f},v={1:8.2f}".format(x,v)

def CreateParticles(numberOfParticles):
    particles = [ ]
    for i in range(numberOfParticles):
        particles.append(Particle(numberOfParticles))
    return particles

def startSimulation(frames, data, numberOfElectrons, messages, iterationsPerFrame, dt, period):
    particles = CreateParticles(numberOfElectrons + 1)
    protonNumber = numberOfElectrons
    initializeParticles(particles)
    for frame in range(frames):
        print "Frame {0}: ".format(frame),
        for iteration in range(iterationsPerFrame):
            determinePathsOfElectrons(particles, protonNumber, dt, magic=1)
            writeInfo(messages, frame, particles)
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
    numberOfElectrons = 2
    particles = numberOfElectrons + 1
    dt = 1
    frames = 10000
    iterationsPerFrame = 1
    dimensions = 3
    messages = [None]*frames
    data = np.zeros(frames * dimensions * particles, dtype=float)
    data = data.reshape(frames, dimensions, particles)
    data = startSimulation(frames, data, numberOfElectrons, messages, iterationsPerFrame, dt, period)
#    data = addParticleTrail(data, frames, electron, electronTrail)
    setupPlot(messages, frames, scale, data)
    

main()
