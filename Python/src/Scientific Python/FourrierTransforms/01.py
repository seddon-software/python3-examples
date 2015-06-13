import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from math import cos, sin, pi

T = 10.0
COEFFS = 14
# square wave function
def f(x):
    xx = x % T
    if xx >= T/2.0:
        return 1
    else:
        return 0

lo = -4.0 * T
hi = +4.0 * T

# compute Fourier coefficents
A = np.array([(2.0 / T) * quad(lambda t : f(t)*cos(2*pi*m*t/T), 0, T)[0] for m in range(COEFFS)])
B = np.array([(2.0 / T) * quad(lambda t : f(t)*sin(2*pi*m*t/T), 0, T)[0] for m in range(COEFFS)])
# print Fourier coefficents (note most of the a's are zero and even b's are zero)
for i, a in enumerate(A): print "a{0} = {1:7.4f}".format(i, a)
for i, b in enumerate(B): print "b{0} = {1:7.4f}".format(i, b)

# calculate the function arrays
X = np.arange(lo, hi, 0.01)
Y = [f(x) for x in X]

# compute the successive fourier approximations 
G = [0] * COEFFS
G[0] = A[0] * np.cos(2*pi*0*X/T) / 2.0
G[1] = G[0] + B[1] * np.sin(2*pi*1*X/T)
for n in range(3, 15, 2):
    G[n] = G[n-2] + B[n] * np.sin(2*pi*n*X/T)


# plot the first few approximations (n.b. missing terms don't contribute
plt.figure(1)
plt.subplot(10,1,1)
plt.plot(X, Y, color='red', lw=2)
plt.plot(X, G[0], color='blue', lw=1)

for i in range(2, 9):
    print 2*i-3
    plt.subplot(10,1,i)
    plt.plot(X, Y, color='red', lw=2)
    plt.plot(X, G[2*i-3], color='blue', lw=1)
    
plt.show()
