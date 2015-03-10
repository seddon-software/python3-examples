############################################################
#
#    Inheritance
#
############################################################


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def WhereAmI(self):
        print "Point(%i) is at %i,%i" % (id(self), self.x, self.y)

    def MoveBy(self, dx, dy):
        self.x += dx
        self.y += dy

class ColoredPoint(Point):
    def __init__(self, x, y, color):
        Point.__init__(self, x, y)
        self.color = color
        
    def ChangeColor(self, newColor):
        self.color = newColor
    
    def Display(self):
        self.WhereAmI()
        print " ... and color is %s" % self.color
        

def WhereAreYou(p):
    p.WhereAmI()

p = Point(5,8)
cp = ColoredPoint(15,25,"Blue")
p.WhereAmI()
cp.Display()

cp.ChangeColor("Cyan")
cp.MoveBy(5,15)
cp.Display()

WhereAreYou(p)
WhereAreYou(cp)
