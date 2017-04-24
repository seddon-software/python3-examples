############################################################
#
#    polynomials
#
############################################################

# pylab is a combination of numpy and matplotlib.pyplot
import pylab as p

""" calculate polynomial: y = -2x^2 + 1 """

X = p.arange(-4, 4, 0.01)
Y = [-2*a**2+1 for a in X]
p.plot(X, Y, color='red', lw=1)
p.gcf().canvas.set_window_title('Calculate Polynomial')

p.show()

