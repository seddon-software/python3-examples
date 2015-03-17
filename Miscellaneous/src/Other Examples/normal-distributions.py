############################################################
#
#    Normal Distribution
#
############################################################

from math import exp, sqrt, pi
from random import random
import Gnuplot

def P(x):
    return exp(-x*x/2.0) / sqrt(2 * pi)

data = []
size = 10000
for x in range(size):
    r = 10.0
    n = r * random() - r / 2.0
    y = P(n)
    data.append([x,y])
        
sortedData = sorted(data, key=lambda data: data[1])

data = []
for x, pt in zip(range(size),sortedData):
    data.append([x,pt[1]])
    
gp = Gnuplot.Gnuplot(debug=1)
gp('set data style points')
gp.plot(data)

1






    
    
