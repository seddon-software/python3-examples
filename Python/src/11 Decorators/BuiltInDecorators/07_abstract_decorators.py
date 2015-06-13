from abc import ABCMeta, abstractmethod, abstractproperty

class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self): pass
	
    @abstractproperty
    def name(self):	pass

class Circle(Shape):
    def __init__(self, name):
		self.theName = name
		
    def display(self):
		print "Circle", self.name
		
    @property
    def name(self):
    	return self.theName
    	
c = Circle("my-circle")
print c.name 
c.display()

try:
	 s = Shape()
except TypeError, e:
	print e
1
