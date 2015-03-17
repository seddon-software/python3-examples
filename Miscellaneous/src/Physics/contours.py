#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from math import *

origin = 'lower'
#origin = 'upper'

delta = 0.025

x = y = np.arange(-3.0, 3.01, delta)
X, Y = np.meshgrid(x, y)


R2 = [x0*x0+y0*y0 for x0 in x for y0 in y]
Z = 10 / (R2)

# We are using automatic selection of contour levels;
# this is usually not such a good idea, because they don't
# occur on nice boundaries, but we do it here for purposes
# of illustration.
CS = plt.contourf(X, Y, Z, 50, # [-1, -0.1, 0, 0.1],
                        #alpha=0.5,
                        cmap=plt.cm.bone,
                        origin=origin)

# Note that in the following, we explicitly pass in a subset of
# the contour levels used for the filled contours.  Alternatively,
# We could pass in additional levels to provide extra resolution,
# or leave out the levels kwarg to use all of the original levels.

# CS2 = plt.contour(CS, levels=CS.levels[::2],
#                         colors = 'r',
#                         origin=origin,
#                         hold='on')

plt.title('Nonsense (3 masked regions)')
plt.xlabel('word length anomaly')
plt.ylabel('sentence length anomaly')

# Make a colorbar for the ContourSet returned by the contourf call.
cbar = plt.colorbar(CS)
cbar.ax.set_ylabel('verbosity coefficient')
# Add the contour line levels to the colorbar
# cbar.add_lines(CS2)




plt.show()

