############################################################
#
#    multiple plots
#
############################################################

import Gnuplot

gp = Gnuplot.Gnuplot()
gp('set data style lines')
 
data1 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16]]    # The first data set (a quadratic)
data2 = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]     # The second data set (a straight line)

# Make the plot items
plot1 = Gnuplot.PlotItems.Data(data1, with_="lines", title="Quadratic")
plot2 = Gnuplot.PlotItems.Data(data2, with_="points 3", title="Linear")

gp.plot(plot1, plot2)


1
