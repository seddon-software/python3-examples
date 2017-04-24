############################################################
#
#    subplots
#
############################################################

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
nrows=3
ncols=1

plot_number=1
plt.subplot(nrows, ncols, plot_number)
plt.plot(t1, f(t1), 'bo')

plot_number=2
plt.subplot(nrows, ncols, plot_number)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plot_number=3
plt.subplot(nrows, ncols, plot_number)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')


plt.show()

1