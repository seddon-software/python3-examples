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

plt.figure(1)
plt.subplot(211)  # 2 rows, 1 column, fig.1
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(212)  # 2 rows, 1 column, fig.2
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.figure(2)
plt.subplot(121)  # 2 rows, 1 column, fig.1
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(122)  # 2 rows, 1 column, fig.2
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.subplot(221)  # 2 rows, 1 column, fig.1
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(222)  # 2 rows, 1 column, fig.2
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.subplot(223)  # 2 rows, 1 column, fig.1
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(224)  # 2 rows, 1 column, fig.2
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.show()

1