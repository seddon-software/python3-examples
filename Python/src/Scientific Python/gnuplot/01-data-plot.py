############################################################
#
#    data plot
#
############################################################


import setup
import Gnuplot

gp = Gnuplot.Gnuplot(debug=1)
gp('set data style lines')

# Pairs of x and y values
data = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16]]    
gp.plot(data)

# Triplets of x,y,z values
data = [[0, 0, 0], [1, 1, 1], [2, 4, 8], [3, 9, 27], [4, 16, 64]]    # Pairs of x and y values
gp.splot(data)

1
