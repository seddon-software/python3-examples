from pyx import *

p = path.line(0, 0, 1, 1)
c = canvas.canvas()
c.stroke(p)

circle = path.circle(0, 0, 2)
c.stroke(circle, [style.linewidth.Thick])

c.writeEPSfile("01")
c.writePDFfile("01")
1
