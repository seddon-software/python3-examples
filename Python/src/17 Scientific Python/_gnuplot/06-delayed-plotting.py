############################################################
#
#    delayed plotting
#
############################################################

from numpy import *
import Gnuplot, math
import time



def f(x):
    return (11*x - 6)*(2*x - 3)

gp = Gnuplot.Gnuplot(debug=0)

x = arange(10, dtype='float_')
y = x**2

# save plots for displaying later
plot1 = Gnuplot.Data(x, y, title='squares', with_='points 3 3')
plot2 = Gnuplot.Func('x**2', title='calculated by gnuplot')

# Plot
gp.title('The function x**2')
gp.xlabel('x')
gp.ylabel('x**2')

min = -1000
max = +1000

# keep replotting graph to animate
for i in range(min, max):
    x = i
    y = f(x)
    plot1 = Gnuplot.Data([min,x,max], [0,y,f(max)], with_='points 1 3')
    gp.plot(plot1)
    time.sleep(0.01)
    

1
