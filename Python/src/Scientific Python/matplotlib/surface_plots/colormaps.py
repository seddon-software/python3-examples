from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)


colormaps = [cm.autumn, cm.bone, cm.cool, cm.coolwarm, cm.copper, cm.flag, cm.gray, cm.hot,     # @UndefinedVariable
             cm.hsv, cm.jet, cm.pink, cm.prism, cm.spring, cm.summer, cm.winter]                # @UndefinedVariable

for cmap in colormaps:
    fig = plt.figure()
#     ax = fig.gca(projection='3d')
    ax = Axes3D(fig)
    surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap, linewidth=0, antialiased=False)
    ax.set_title(cmap.name)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surface, shrink=0.5, aspect=5)
    plt.show()

