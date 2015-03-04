from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

X = [[ 0, 1, 2, 3],[ 0, 1, 2, 3],[ 0, 1, 2, 3],[ 0, 1, 2, 3]]
Y = [[ 0, 0, 0, 0],[ 1, 1, 1, 1],[ 2, 2, 2, 2],[ 3, 3, 3, 3]]
Z = [[15,16,17,18],[17,20,23,27],[19,22,28,36],[21,26,26,29]]

# plot surface
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.3)
# rstride and cstride are the row and column strides
# the stride determines how many points define the edge of a surface
# rstride = 4, cstride = 8 means the surface consists or the region between 4 rows and 8 columns

# plot filled contours on z = 5 axis
cset = ax.contourf(X, Y, Z, zdir='z', offset=5, cmap=cm.coolwarm)  # @UndefinedVariable

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.5, 3.5)
ax.set_zlim(0, 30)

plt.show()

