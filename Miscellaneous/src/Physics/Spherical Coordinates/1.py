from scipy import integrate
import numpy as np
import math
from pylab import sqrt, trapz, pi, exp, cos, sin, arccos, arctan2, plt


def modulus(x_):
    return sqrt(x_.dot(x_))

def CartesianToSpherical(cartesian_):
    x = cartesian_[0]
    y = cartesian_[1]
    z = cartesian_[2] 
    r = sqrt(x*x + y*y + z*z)
    if r == 0: raise Exception("conversion not possible at origin")
    theta = arccos(z/r)
    # phi is troublesome when x = 0
    try:
        phi = arctan2(y, x)
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

def length(x1_, x2_):
    c1_ = SphericalToCartesian(x1_)
    c2_ = SphericalToCartesian(x2_)
    return modulus(c1_ - c2_)

def lengths(*es_):
    for e1_ in es_:
        for e2_ in es_:
            if id(e1_) != id(e2_): 
                print length(e1_, e2_),
                printV(SphericalToCartesian(e1_))
                printV(SphericalToCartesian(e2_))
def main():
    e1_ = CartesianToSpherical([+10, 0, 0])
    e2_ = CartesianToSpherical([-10, 0, 0])
    e1a_ = CartesianToSpherical([0, +10, 0])
    e2a_ = CartesianToSpherical([0, -10, 0])
    printV(e1_)
    printV(e2_)
    print
    e1_ = [10, pi/2, 0*pi/180]
    e2_ = [20, pi/2, 50*pi/180]
    e3_ = [20, pi/2, 60*pi/180]
    e4_ = [20, pi/2, 120*pi/180]
    e5_ = [20, pi/2, -120*pi/180]
    e6_ = [20, pi/2, -60*pi/180]
    lengths(e1_, e2_)
#     lengths(e1_, e2_, e1a_, e2a_)
#     lengths(e1_, e2_, e3_, e4_, e5_, e6_)
    
def printV(v_):
    print "[{0:8.3f},".format(v_[0]),
    print "{0:8.3f},".format(v_[1]),
    print "{0:8.3f}] ".format(v_[2]),
    
def debug(spherical_):
    printV(spherical_)
    cartesian_ = SphericalToCartesian(spherical_)
    printV(cartesian_)
    spherical_ = CartesianToSpherical(cartesian_)
    printV(spherical_)
    print
    
main()
