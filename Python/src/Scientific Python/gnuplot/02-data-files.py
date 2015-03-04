############################################################
#
#    data files
#
############################################################

import Gnuplot

try:
    gp = Gnuplot.Gnuplot()
except Exception, e:
    print e
    
f = open("data/f1.dat")

# read in the data points
data = []
for line in f:
    point = line.split()
    data.append(point)

# plot them
gp.plot(data)

1
