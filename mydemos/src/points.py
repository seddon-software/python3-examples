import pprint

class Point:
    count = 0
    def getCount():
        return Point.count
    def __init__(self, x0, y0, name):  # CTOR
        Point.count += 1
        self.x = x0
        self.y = y0
        self.name = name
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    def display(self):
        print( "Point:{2} [{0},{1}]".format(self.x, self.y, self.name) )
# create objects (instances of the class)

class A: pass

print( Point.getCount() )
p1 = Point(100, 200, 'point-p1')
p1.__class__ = A
p2 = Point(110, 210, 'point-p2')
p3 = Point(120, 220, 'point-p3')
print(Point)
pprint.pprint(Point.__dict__)
print(Point.__bases__)
print(p1.__dict__)
print( Point.getCount() )
p1.moveBy(2, 2)
p2.moveBy(1, 1)
p3.moveBy(1, 1)
p1.display()
p2.display()
p3.display()

