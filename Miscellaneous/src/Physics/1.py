import numpy as np
from numpy import array, dot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt, sin, cos

def update_plot(frame, data, sc):
    sc._offsets3d = data[frame]
    return sc


def main():
    proton = 0
    electron = 1
    
    frames = 2000
    dimensions = 3
    particles = 20
    data = np.ones(frames * dimensions * particles)
    data = data.reshape(frames, dimensions, particles)
    
    for particle in range(particles):
        for dimension in ['x', 'y', 'z']:
            for frame in range(frames): 
                data[frame][0][proton] = 0
                data[frame][1][proton] = 0
                data[frame][2][proton] = 0

                r = 200
                theta = frame * 0.1
                x = r * sin(theta)
                y = r * cos(theta)
                # particle 0 is the proton, particle 1 is the electron, the others are the electron's previous positions
                if particle == 1:
                    if dimension == 'x': data[frame][0][electron] = x
                    if dimension == 'y': data[frame][1][electron] = y
                    if dimension == 'z': data[frame][2][electron] = 100
                elif particle > 1 and frame > particles:
                    data[frame][0][particle] = data[frame-particle + 1][0][electron]
                    data[frame][1][particle] = data[frame-particle + 1][1][electron]
                    data[frame][2][particle] = data[frame-particle + 1][2][electron]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d([-250.0, 250.0])
    ax.set_ylim3d([-250.0, 250.0])
    ax.set_zlim3d([-250.0, 250.0])
    ax.set_autoscale_on(False)


    ix, iy, iz = data[0]
    sc = ax.scatter(ix, iy, iz, s=100.0, c='red', marker='d')
    ani = FuncAnimation(fig, update_plot, frames=frames, fargs=(data,sc), interval=100)
    plt.show()


main()
    