# Point
#   Attributes: x, y, color, name
#   Methods:    initialize, moveBy, display

class Point(object):
    count = 0
    @staticmethod
    def getCount():
        return Point.count
    def __init__(self, x0, y0, color, name):
        Point.count += 1
        self.x = x0
        self.y = y0
        self.color = color
        self.name = name
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    def display(self):
        print("{3}: [{0},{1}], color={2}".format(self.x, self.y, self.color, self.name))
# create objects
q = Point('green', 'origin')
p1 = Point(100, 200, 'blue', 'point-p1')
p2 = Point(101, 201, 'cyan', 'point-p2')
p3 = Point(102, 202, 'orange', 'point-p3')
print(Point.getCount())
p1.moveBy(10, 10)
p2.moveBy(10, 10)
p3.moveBy(10, 10)
p1.display()
p2.display()
p3.display()

1

