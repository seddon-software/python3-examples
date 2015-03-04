from numpy import *
import pylab as p
#import matplotlib.axes3d as p3
import mpl_toolkits.mplot3d.axes3d as p3

# r_[start:stop:cstep]
#     if step is an imaginary number (i.e. 100j) then its integer portion is interpreted as a number-of-points desired and the start and stop are inclusive
#     in other words start:stop:stepj is interpreted as np.linspace(start, stop, step, endpoint=1)


# u and v are parametric variables.
u=r_[0:2*pi:50j] # an array from 0 to 2*pi, with 50 elements
v=r_[0:pi:25j]   # an array from 0 to pi, with 25 elements

x=10*outer(cos(u),sin(v))
y=10*outer(sin(u),sin(v))
z=10*outer(ones(size(u)),cos(v))


fig=p.figure()
ax = p3.Axes3D(fig)
ax.plot_wireframe(x,y,z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
p.show()
