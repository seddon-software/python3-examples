############################################################
#
#    polynomials
#
############################################################

# pylab is a combination of numpy and matplotlib.pyplot
import pylab as p

""" calculate polynomial: y = -2x^2 + 1 """

x = p.arange(-4, 4, 0.01)
y = [-2*a**2+1 for a in x]
p.plot(x,y, color='red', lw=1)
p.show()

