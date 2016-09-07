############################################################
#
#    vector fields
#
############################################################

import Gnuplot

gp = Gnuplot.Gnuplot()

# Generate the vector field data
data = []
for i in range(-10, 11):
   for j in range(-10, 11):
      data.append([i/10., j/10., -i/100., -j/100.]) # Each data entry has the form [x, y, u, v]

# Plot everything: note that the with argument is 'vectors'
plot = Gnuplot.PlotItems.Data(data, with_ = 'vectors')
gp.plot(plot)


1
