import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt, sin, cos, pi


def update_plot(frame, data, sc, ax, messages):
    frame = frame + 4900
    sc._offsets3d = data[frame]
    ax.set_xlabel(str(frame) + ' X: ' + messages[frame])
    return sc, ax

X = 0
Y = 1
Z = 2

def determinePathOfProton(data, frames, particleNumber):
    for frame in range(frames):
        data[frame][X][particleNumber] = 0.0
        data[frame][Y][particleNumber] = 0.0
        data[frame][Z][particleNumber] = 0.0
    return data


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


''' x is position vector '''
def electricField(x, period):
    k = period
    r = modulus(x)
    rHat = x / r
    force =  func(r, period) * rHat
    return force

def lorentzForce2(X, v_, period, dve_):
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

def lorentzForce(X, v_, period, dve_):
    # when electric K = 100
    k = period # 10000 # 531 to 8834  = orbit 1, 8835-25800 = orbit 2, 25801-25899 unstable, 25900-30000 = orbit 3
    x = modulus(X)
    zeta = sin(x * pi / period)
    v = modulus(v_)
    delta = 0.000001
    if v < delta: 
        print "low velocity"
        return np.array([0.0, 0.0, 0.0])
    vHat_ = v_ / v
    dve = modulus(dve_)
    if dve < delta:
        return np.array([0.0, 0.0, 0.0])
        
    vHat_ = dve_ / dve
    zHat_ = np.array([0.0, 0.0, 1.0])
    k = k * 1000
    force_ =  np.cross(zHat_, dve_) * k  / x
    return force_

def determinePathOfElectron(messages, data, frames, iterationsPerFrame, dt, particleNumber, period, nucleusCharge):
    # initial position and velocity
    electronPosition_ = np.array([1250.0, 0.0, 200.0])
    electronVelocity_ = np.array([-0.01, -0.01, 0.0])
    dve_ = np.array([0.0, 0.0, 0.0])
    
    dvm_ = lorentzForce(electronPosition_, electronVelocity_, period, dve_)
    for frame in range(frames):
        for iteration in range(iterationsPerFrame):
            dve_ = electricField(electronPosition_, period)
            dvmPrevious_ = dvm_
            dvm_ = lorentzForce(electronPosition_, electronVelocity_, period, dve_)
            dv_ = (dve_ + dvm_) * nucleusCharge
            electronVelocity_ = electronVelocity_ + dv_
            electronPosition_ = electronPosition_ + electronVelocity_ * dt
            x = modulus(electronPosition_)
            v = modulus(electronVelocity_)
            if x < 10: raise Exception("hit origin")
            messages[frame] = "x={0:8.2f},v={1:8.2f},E={2:6.3f},{3:6.3f},{4:6.3f},B={5:6.3f},{6:6.3f},{7:6.3f},".format(x,v,dve_[0],dve_[1],dve_[2],dvm_[0],dvm_[1],dvm_[2])
        print frame, x
        data[frame][X][particleNumber] = electronPosition_[0]
        data[frame][Y][particleNumber] = electronPosition_[1]
        data[frame][Z][particleNumber] = electronPosition_[2]
    return data

def main():
    scale = 100
    period = 50
    proton = 0
    electron = 1
    electronTrail = 0
    particles = electron + electronTrail + 1
    dt = 1
    frames = 10000
    iterationsPerFrame = 1
    dimensions = 3
    messages = [None]*frames
    data = np.zeros(frames * dimensions * particles, dtype=float)
    data = data.reshape(frames, dimensions, particles)
    data = determinePathOfProton(data, frames, proton)
    nucleusCharge = 0.5
    data = determinePathOfElectron(messages, data, frames, iterationsPerFrame, dt, electron, period, nucleusCharge)
    data = addParticleTrail(data, frames, electron, electronTrail)
    setupPlot(messages, frames, scale, data)
    

main()
