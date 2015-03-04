############################################################
#
#    multiple plots
#
############################################################

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0.0, 5.0, 0.200)

redDashes = "r--"
blueSquares = "bs"
greenTriangles = "g^"
plt.plot(t, t,    redDashes, 
         t, t**2, blueSquares,  
         t, t**3, greenTriangles)
plt.show()

1