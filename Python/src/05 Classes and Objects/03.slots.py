class Point(object):
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print "x, y = ", self.x, self.y        


try:
    p = Point(10, 20)
    p.display()
    print p.__slots__
#    print p.__dict__
    p.z = 50        # not allowed
except AttributeError, e:
	print e


1
