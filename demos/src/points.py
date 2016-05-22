class Point:
    def __init__(self, x0, y0):  # constructor 
        self.x = x0
        self.y = y0
    def moveBy(self, dx, dy): # method
        self.x += dx
        self.y += dy
    def display(self):
        print "{},{}".format(self.x, self.y)
        
p1 = Point(100, 200)
p2 = Point(110, 210)
p3 = Point(120, 220)
p1.moveBy(5, 10)
p2.moveBy(3, 7)
p3.moveBy(1, 6)
p1.display()
p2.display()
p3.display()

