class Point(object):
    count = 0
    def __init__(self, name, x0 = 0, y0 = 0):
        """CTOR"""
        Point.count = Point.count + 1 
        self.x = x0
        self.y = y0
        self.name = name
    @staticmethod
    def getCount():
        return Point.count
    def display(self):
        print "Point:'{0}' is at [{1},{2}]".format(self.name, self.x, self.y)
    def moveBy(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
# create dem objects
print Point.getCount()
p1 = Point('point 1', 100, 200)
p2 = Point('point 2')
p3 = Point('point 3', 120, 220)
print Point.getCount()
p1.count = p1.count 
p1.moveBy(dy = 9, dx = 11)
p2.moveBy(dy = 9, dx = 11)
p3.moveBy(dy = 9, dx = 11)

p1.display()
p2.display()
p3.display()



1
