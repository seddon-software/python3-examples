from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)


"""
Possible marker types:
    's' : square
    'o' : circle
    '^' : triangle up
    '>' : triangle right
    'v' : triangle down
    '<' : triangle left
    'd' : diamond
    'p' : pentagram
    'h' : hexagon
    '8' : octagon
"""
markers = ['s', 'o', '^', '>', 'v', '<', 'd', 'p', 'h', '8']


for i, marker in enumerate(markers):
    ax.scatter([i], [i], s = 500, marker=marker)
plt.show()

