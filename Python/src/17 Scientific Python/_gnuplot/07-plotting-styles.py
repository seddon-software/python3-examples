############################################################
#
#    plotting styles
#
############################################################

from numpy import *
import Gnuplot
import math



gp = Gnuplot.Gnuplot(debug=1)

x = arange(10, dtype='float_')
y = x**2

# save plots for displaying later
plot1 = Gnuplot.Func('x**2/100.', title='x**2', with_='boxes')
plot2 = Gnuplot.Func('cos(x)', title='cos(x)', with_='lines')
plot3 = Gnuplot.Func('norm(x)', title='norm(x)', with_='errorbars')

# Plot
gp.title('Various functions and styles')
gp.xlabel('x')
gp.ylabel('y')
gp.plot(plot1, plot2, plot3)


1
