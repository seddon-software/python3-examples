import numpy as np
from numpy import array, dot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt, sin, cos, pi

def update_plot(frame, data, sc):
    sc._offsets3d = data[frame]
    return sc

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
   particle must be a 3D NumPy array, n is particle number
"""
def determinePathOfElectron(data, frames, dt, particleNumber):
    electronPosition = np.array([75.0, 80.0, 0.0])
    electronVelocity = np.array([-0.1, 0.1, 0.0])
    rmin = 1000.0
    rmax = 0.0
    
    k = 60
    dv = np.array([0.0, 0.0, 0.0])
    for frame in range(frames):
        t = frame * dt
        e = electronPosition
        r = sqrt(e[0]*e[0] + e[1]*e[1] + e[2]*e[2])
        
        # try some force fields
        if r < 10: 
            electronVelocity = np.array([0.0, 0.0, 0.0])
            electronPosition = np.array([0.0, 0.0, 0.0])
        else:
            rhat = e / r
            zeta = cos(r * pi / 50.0)
            dv = rhat * [-k/(r*r)] * abs(zeta)
            dv = rhat * [-k/(r*r)]
            dv = rhat * [-k/(r*r)] * zeta * zeta
            dv = rhat * [-k/(r*r)] * zeta
            electronVelocity = electronVelocity + dv
            electronPosition = electronPosition + electronVelocity * dt
        if r > rmax:
            rmax = r
            print "rmax=", rmax
        if r < rmin:
            rmin = r
            print "rmin=", rmin    
        data[frame][x_][particleNumber] = electronPosition[0]
        data[frame][y_][particleNumber] = electronPosition[1]
        data[frame][z_][particleNumber] = electronPosition[2]
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
    

def setupPlot(frames, data):
    fig = plt.figure()
    fig = plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
    fig.set_size_inches(8.5,4.5)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    drawCircles(ax, 50, 10)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d([-250.0, 250.0])
    ax.set_ylim3d([-250.0, 250.0])
    ax.set_zlim3d([-250.0, 250.0])
    ax.set_autoscale_on(False)
    ix, iy, iz = data[0]
    sc = ax.scatter(ix, iy, iz, s=100.0, c='red', marker='o')
    ani = FuncAnimation(fig, update_plot, frames=frames, fargs=(data, sc), interval=10)
    plt.show()

def main():
    proton = 0 
    electron = 1
    electronTrail = 1
    particles = electron + electronTrail + 1
    dt = 10
    frames = 20000
    dimensions = 3
    data = np.zeros(frames * dimensions * particles, dtype=float)
    data = data.reshape(frames, dimensions, particles)
    data = determinePathOfProton(data, frames, proton)
    data = determinePathOfElectron(data, frames, dt, electron)
    data = addParticleTrail(data, frames, electron, electronTrail)
    setupPlot(frames, data)
    

main()
    