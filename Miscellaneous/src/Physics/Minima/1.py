from scipy import integrate
import numpy as np
import math
#from pylab import *
#from scipy.integrate import quad
from pylab import sqrt, trapz, pi, exp, cos, sin, arccos, arctan2, plt
from _imaging import path


def modulus(x_):
    return sqrt(x_.dot(x_))

def proton2electron(r, period, charge):
    z = 0
    h = r / period
    for n in range(0, 9):
        s = r - n * period
        z = z + exp(-s*s) / (h * h)
    return z * charge

def electron2electron(r, period, charge):
    h = r / period
    return 1/(h*h) * charge - proton2electron(r, period, charge)
 

class Particle:
    def __init__(self, x_, charge, type):
        self.x_ = x_
        self.charge = charge
        self.type = type
    
def Force(particle1, particle2, period):
    x_ = particle1.x_ - particle2.x_
    x = modulus(x_)
    xHat_ = x_ / x
    if particle2.type == 'proton':
        return xHat_ * proton2electron(x, period, particle2.charge)
    else:
        return xHat_ * electron2electron(x, period, particle2.charge)
        
    
def SumForces(testParticle, existingParticles, period): 
    force_ = np.array([0.0, 0.0, 0.0])   
    for particle in existingParticles:
        z_ = Force(testParticle, particle, period)
        force_ = force_ + Force(testParticle, particle, period)
    return force_

def CartesianToSpherical(cartesian_):
    x = cartesian_[0]
    y = cartesian_[1]
    z = cartesian_[2] 
    r = sqrt(x*x + y*y + z*z)
    if r == 0: raise Exception("conversion not possible at origin")
    theta = arccos(z/r)
    # phi is troublesome when x = 0
    try:
        phi = arctan2(x, y)
    except:
        raise "divide by zero"
    return np.array( [r, theta, phi] )

def SphericalToCartesian(spherical_):
    r = spherical_[0]
    theta = spherical_[1]
    phi = spherical_[2]
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return np.array( [x, y, z] )

def printSpherical(name, cartesian_):
    spherical_ = CartesianToSpherical(cartesian_)
    r = spherical_[0]
    theta = spherical_[1] * 180.0 / pi
    phi = spherical_[2] * 180.0 / pi
    print "{0}(r,theta,phi) = {1:6.2f}, {2:6.2f}, {3:6.2f}".format(name, r, theta, phi)

def main():
#     c1_ = np.array( [+10.0, 0.0, 0.0] )
#     c2_ = np.array( [-10.0, 0.0, 0.0] )
#     s1_ = CartesianToSpherical(c1_)
#     s2_ = CartesianToSpherical(c2_)
    n = 3
    proton = Particle( np.array([0.0, 0.0, 0.0]), n, 'proton')
    e1 = Particle( np.array([+10.0, 0.0, 0.0]), -1, 'electron')
    e2 = Particle( np.array([-10.0, 0.0, 0.0]), -1, 'electron')
    printSpherical("e1", e1.x_)
    printSpherical("e2", e2.x_)
    
    particles = [proton, e1, e2]
    # determine minima of force in 2nd shell
    period = 10
    radius = 2 * period
    numberOfPoints = 40
    theta0 = 165.0 * pi / 180.0
    theta1 = 170.0 * pi / 180.0
    phi0 = 9.85 * pi / 180.0
    phi1 = 9.9 * pi / 180.0
    thetas = [ theta  * 180.0 / pi for theta in np.linspace(theta0, theta1, numberOfPoints) ]
    phis = [ phi  * 180.0 / pi for phi in np.linspace(phi0, phi1, numberOfPoints) ]
    forces = [ ]
    
    for theta in thetas:
        theta = theta * pi / 180.0
        for phi in phis:
            phi = phi * pi / 180.0
            x = radius * sin(theta) * cos(phi)
            y = radius * sin(theta) * sin(phi)
            z = radius * cos(theta)
            e3 = Particle( np.array([x, y, z]), -1, 'electron')
            force_ = SumForces(e3, particles, period)
            forces.append(modulus(force_))
    plotGraph(thetas, phis, forces)
      
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
  
def plotGraph(X, Y, Z):    
    fig = plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
    fig.set_size_inches(15.5, 11.5)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    X, Y = np.meshgrid(X, Y)
    Z = np.reshape(Z, X.shape)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_xlabel('theta')
    ax.set_ylabel('phi')
#     for angle in np.linspace(0, 90, 10):
#         print angle
#         ax.view_init(elev=30., azim=angle)
#         plt.savefig("plots/plot_{0:02.0f}.png".format(angle))
    ax.view_init(elev=15.0, azim=10.0)
    plt.show()
  
main()
