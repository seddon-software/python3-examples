class Point:
    count = 0
    @staticmethod
    def getCount():
        return Point.count
    def __init__(self, name, x0=0, y0=0):
        Point.count += 1
        self.name = name
        self.x = x0
        self.y = y0
    def display(self):
        print "{:12s}[{},{}]".format(self.name, self.x, self.y)
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
q = Point("origin")
p1 = Point("wendy", 12, 10)
p2 = Point("peter", 22, 20)
p3 = Point("tinkerbell",  32, 30)
p1.moveBy(100, 100)
p2.moveBy(100, 100)
p3.moveBy(100, 100)
q.display()
p1.display()
p2.display()
p3.display()
# print p1.name
# print p1.__dict__['name']


1

