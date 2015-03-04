############################################################
#
#    hardcopies
#
############################################################

import Gnuplot
import math


gp = Gnuplot.Gnuplot()

# Generate the vector field data
data = []
for i in range(-10, 11):
    for j in range(-10, 11):
        data.append([i/100., math.sin(j)/100., -i/10., -math.cos(j)/10.]) # Each data entry has the form [x, y, u, v]
# Plot everything: note that the with argument is 'vectors'
plot = Gnuplot.PlotItems.Data(data, with_ = 'vectors')
gp.plot(plot)

gp.hardcopy(filename="data/mygraph.ps",terminal="postscript") 

1
