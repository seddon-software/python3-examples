import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt, sin, cos, pi


def update_plot(frame, data, sc, ax, messages):
    sc._offsets3d = data[frame]
    ax.set_xlabel(str(frame) + ' X: ' + messages[frame])
    return sc, ax

x_ = 0
y_ = 1
z_ = 2

"""
   particle must be a 3D NumPy array, n is particle number
"""
def determinePathOfProton(data, frames, particleNumber):
    for frame in range(frames):
        data[frame][x_][particleNumber] = 0.0
        data[frame][y_][particleNumber] = 0.0
        data[frame][z_][particleNumber] = 0.0
    return data


"""
   particle must be a 3D list, trailCount determines how many previous frames are included in the trail
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
    for r in range(r0, r0 * n, r0):
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
    fig = plt.figure()
    fig = plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
    fig.set_size_inches(8.5,4.5)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    drawCircles(ax, scale, 5)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    max = 5 * scale / 2.0
    ax.set_xlim3d([-max, max])
    ax.set_ylim3d([-max, max])
    ax.set_zlim3d([-max, max])
    ax.set_autoscale_on(False)
    ix, iy, iz = data[0]
    sc = ax.scatter(ix, iy, iz, s=100.0, c='red', marker='o')
    ani = FuncAnimation(fig, update_plot, frames=frames, fargs=(data, sc, ax, messages), interval=100, blit=True)
    plt.show()

def modulus(x):
    return sqrt(x.dot(x))

def func(t, period):
    k = period * period
    z = (t  + period / 2) % period - period / 2
    upper = 1
    lower = - 1
    if z < upper and z > lower:
        result = -k * cos(z * pi / 2) / (t * t)
    else:
        result = 0
    return result


''' x is position vector '''
def electricField(x):
    k = 100
    r = modulus(x)
    rHat = x / r
    if r < 10: raise Exception("hit origin")
#     zeta = sin(r * pi / 50.0)
#     f = -k / (r * r)
    force =  func(r, 50.0) * rHat
    return force

def magneticField(x, origin):
    k = 5000
    r = modulus(x - origin)
    rHat = (x - origin) / r
    if r < 10: raise Exception("hit origin")
    zeta = cos(r * pi / 50.0)
    zeta = sin(r * pi / 50.0)
    zeta = 1
    f = -k / (r * r)
    force =  (zeta * zeta * f) * rHat
    return force

def lorentzForce(x_, v_):
    delta = 0.000001
    k = 1000
    x = modulus(x_)
    if x < 10: raise Exception("hit origin")
    zeta = sin(x * pi / 50.0)
    v = modulus(v_)
    if v < delta: 
        print "low velocity"
        return np.array([0.0, 0.0, 0.0])
    vHat_ = v_ / v
    zHat_ = np.array([0.0, 0.0, 1.0])
    force_ =  np.cross(zHat_, vHat_) * zeta * zeta * k * v / (x * x)
    return force_

def determinePathOfElectron(messages, data, frames, iterationsPerFrame, dt, particleNumber):
    delta = 0.000001
    # initial position and velocity
    electronPosition = np.array([325.0, 0.0, 100.0])
    electronVelocity = np.array([-0.01, 0.0, -0.003])
    
    dvm = lorentzForce(electronPosition, electronVelocity)
#     northPole = np.array([0.0, 0.0, 1.0])
#     southPole = np.array([0.0, 0.0, -1.0])
    for frame in range(frames):
        for iteration in range(iterationsPerFrame):
            dve = electricField(electronPosition)
#             magneticForce = magneticField(electronPosition, northPole) - magneticField(electronPosition, southPole) 
#             try:
#                 if modulus(electronVelocity) > delta:
#                     electronVelocityHat = electronVelocity / modulus(electronVelocity)
#                     dvm = np.cross(magneticForce, electronVelocityHat)
#                 else:
#                     dvm = np.array([0.0, 0.0, 0.0])
#             except:
#                 print "********** Problems in calculation **********"
            dvmPrevious = dvm
            dvm = lorentzForce(electronPosition, electronVelocity)
            dv = dve + dvm - dvmPrevious
            electronVelocity = electronVelocity + dv
            electronPosition = electronPosition + electronVelocity * dt
            x = modulus(electronPosition)
            v = modulus(electronVelocity)
            print x
            messages[frame] = "x={0:8.2f},v={1:8.2f},E={2:6.3f},{3:6.3f},{4:6.3f},B={5:6.3f},{6:6.3f},{7:6.3f},".format(x,v,dve[0],dve[1],dve[2],dvm[0],dvm[1],dvm[2])
        data[frame][x_][particleNumber] = electronPosition[0]
        data[frame][y_][particleNumber] = electronPosition[1]
        data[frame][z_][particleNumber] = electronPosition[2]
    return data

def main():
    scale = 100
    proton = 0 
    electron = 1
    electronTrail = 1
    particles = electron + electronTrail + 1
    dt = 1
    frames = 100000
    iterationsPerFrame = 5
    dimensions = 3
    messages = [None]*frames
    data = np.zeros(frames * dimensions * particles, dtype=float)
    data = data.reshape(frames, dimensions, particles)
    data = determinePathOfProton(data, frames, proton)
    data = determinePathOfElectron(messages, data, frames, iterationsPerFrame, dt, electron)
    data = addParticleTrail(data, frames, electron, electronTrail)
    setupPlot(messages, frames, scale, data)
    

main()
