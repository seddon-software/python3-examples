class Point:
    count = 0
    @staticmethod
    def getCount():
        return Point.count        
    def __init__(self, x0, y0, name):
        Point.count += 1
        self.x = x0
        self.y = y0
        self.name = name
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    def display(self):
        print(self.x, self.y, self.name)

# create some objects
p1 = Point(100, 200, 'point-p1')
p2 = Point(110, 240, 'point-p2')
p3 = Point(130, 220, 'point-p3')
p1.count = p1.count
print(p1.getCount())
print(Point.getCount())
p1.moveBy(1, 1)
p2.moveBy(1, 1)
p3.moveBy(1, 1)
p1.display()
p2.display()
p3.display()



1
