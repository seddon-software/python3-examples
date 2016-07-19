# pylab is for interactive use and includes an implicit import of numpy
import matplotlib.pylab as pl

    
def main():
    pl.ion()     # interactive mode
    fig1 = pl.figure()
    ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    pl.draw()
    ax1.plot(pl.arange(5), [30, 40, 55, 80, 100])
    pl.draw()
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    pl.draw()
    
    for label in ax1.get_xticklabels():
        label.set_color('red')
        pl.draw()

    for label in ax1.get_yticklabels():
        label.set_color('green')
    pl.draw()
    ax1.grid(True)
    pl.draw()
    ax1.patch.set_facecolor('yellow')
    pl.draw()

    fig2 = pl.figure()
    pl.draw()
    ax2 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
    pl.draw()
    t = pl.arange(0.0, 1.0, 0.01)
    s = pl.sin(2*pl.pi*t)
    ax2.plot(t, s, color='blue', lw=2)
    pl.draw()
    print "done"
main()
