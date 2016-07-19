class Point:
    def initialize(self, x0, y0, name):
        self.x = x0
        self.y = y0
        self.name = name
    
    def display(self):
        print(self.x, self.y, self.name)

# create objects (instances of the class)
p1 = Point()
p2 = Point()
p3 = Point()

p1.initialize(100, 200, 'point-p1')
p2.initialize(110, 210, 'point-p2')
p3.initialize(120, 220, 'point-p3')

p1.display()
p2.display()
p3.display()

