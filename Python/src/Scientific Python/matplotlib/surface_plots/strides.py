from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
n = 100
X = np.arange(n)
Y = np.arange(n)
X = np.expand_dims(X, axis=0)
Y = np.expand_dims(Y, axis=1)

Z = X * Y + X + Y

ax.plot_surface(X, Y, Z, rstride=4, cstride=25, alpha=0.3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(0, n)
ax.set_ylim(0, n)
ax.set_zlim(0, n * n)

plt.show()

