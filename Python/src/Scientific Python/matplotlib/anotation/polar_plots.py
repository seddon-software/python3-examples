############################################################
#
#    polar plots
#
############################################################

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0,1,0.001)
theta = 2*2*np.pi*r

line, = ax.plot(theta, r, color="#ee8d18", lw=3)
index = 600
r0, theta0 = r[index], theta[index]
ax.plot([theta0], [r0], "o")

message = "r=%4.2f theta=%4.2f" % (r0, theta0)
ax.annotate(message,
            xy=(theta0, r0), # theta, radius
            xytext=(0.07, 0.07), # fraction, fraction
            textcoords="figure fraction",
            arrowprops=dict(facecolor="green", shrink=0.02),
            horizontalalignment="left",
            verticalalignment="bottom",
           )
plt.show()

