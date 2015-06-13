class Point(object):
    count = 0
    # CTOR
    @staticmethod
    def getCount():
        return Point.count
    def __init__(self, x0, y0, name):
        Point.count += 1
        self.x = x0
        self.y = y0
        self.name = name
    def __del__(self):
        print 'Not much use'
    def moveBy(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def display(self):
        print '{0} is at [{1},{2}]'.format(self.name, self.x, self.y)

# create some objects

print Point.getCount()
p1 = Point(100, 200, 'Point-p1')
p2 = Point(101, 201, 'Point-p2')
p3 = Point(102, 202, 'Point-p3')
print Point.getCount()

p1.moveBy(1, 1)
p2.moveBy(1, 1)
p3.moveBy(1, 1)
p1.display()
p2.display()
p3.display()




1

