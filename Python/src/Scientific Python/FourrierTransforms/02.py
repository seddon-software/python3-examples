import numpy as np
# import matplotlib.pyplot as plt
import scipy
from scipy.integrate import quad
from math import cos, sin, pi
from scipy import exp

def complex_quadrature(func, a, b, **kwargs):
    def real_func(x):
        return scipy.real(func(x))
    def imag_func(x):
        return scipy.imag(func(x))
    real_integral = quad(real_func, a, b, **kwargs)
    imag_integral = quad(imag_func, a, b, **kwargs)
    return (real_integral[0] + 1j*imag_integral[0], real_integral[1:], imag_integral[1:])

z = complex_quadrature(lambda x: (scipy.exp(1j*x)), 0, scipy.pi/2)
print z[0]

def toZero(c):
    if c.real < 1e-10 and c.imag < 1e-10: c = 0
    return c

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

CC = [0 if n % 2 == 0 else 1/(1j*pi*n) for n in range(1, 20)] 
CC.insert(0, 0.5)

C = [0]*20
for n in range(20):
    C[n] = (1/T) * complex_quadrature(lambda t : f(t)*exp(-2j*pi*n*t/T), T, 0)[0]
    print n, toZero(CC[n] - C[n])
    


