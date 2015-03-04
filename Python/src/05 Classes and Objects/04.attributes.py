import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print "x, y = ", self.x, self.y        

    # always called when getting attribute
    def __getattribute__(self, name):
        if name != "__class__": print "\n*** getting", name
        return object.__getattribute__(self, name)

    # called if __getattribute__ fails
    def __getattr__(self, name):
        print "\n***", name, "attribute not found"
        return 0
        
    # always called when setting attribute        
    def __setattr__(self, name, value):
        print "\n*** setting", name, "=", value
        object.__setattr__(self, name, value)
        
p = Point(10, 20)
p.display()
p.z = 50
p.z = p.a   # p.a call __getattr__()


1
