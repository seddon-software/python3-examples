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

def subplot2x1():
    # 2 rows and 1 col
    plt.subplot(211)  # plot 1
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    plt.subplot(212)  # plot 2
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

def subplot2x3():
    plt.figure()        # create new figure
    # 2 rows and 3 cols
    plt.subplot(2,3,1)  # plot 1
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    plt.subplot(2,3,2)  # plot 2
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.subplot(2,3,3)  # plot 3
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    plt.subplot(2,3,4)  # plot 4
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.subplot(2,3,5)  # plot 5
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    plt.subplot(2,3,6)  # plot 6
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

def subplot3x2():
    plt.figure()        # create new figure
    nrows = 4
    ncols = 2
    for plotNo, style in zip(range(nrows*ncols), ['k', 'r--']*nrows):
        plt.subplot(nrows, ncols, plotNo+1)
        plt.plot(t2, np.cos(2*np.pi*t2), style)

subplot2x1()
subplot2x3()
subplot3x2()
plt.show()

