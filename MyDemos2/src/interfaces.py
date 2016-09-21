from abc import ABC, abstractmethod

# pure contract
# interface
class IShape(ABC):
    @abstractmethod
    def draw(self): pass
    @abstractmethod
    def hide(self): pass
    @abstractmethod
    def show(self): pass

# class designers
# abstract class
class Shape(IShape):
    def draw(self): print("default impl")
    @staticmethod
    def factory(code):
        if code == 0: return Triangle()
        if code == 1: return Ellipse()
        if code == 2: return Rectangle()
        
#concrete class
class Triangle(Shape):
    def draw(self): 
        super(Triangle, self).draw()
        print("Triangle draw")
    def hide(self): print("Triangle hide")
    def show(self): print("Triangle show")
    
class Ellipse(Shape):
    def hide(self): print("Ellipse hide")
    def show(self): print("Ellipse show")

class Rectangle(Shape):
    def draw(self): print("Rectangle draw")
    def hide(self): print("Rectangle hide")
    def show(self): print("Rectangle show")


# class users
def drawAnything(s):
    s.draw()

t = Shape.factory(0)
e = Shape.factory(1)
r = Shape.factory(2)
try:
    s = Shape()
except TypeError as error:
    print(error)
    
drawAnything(t)
drawAnything(e)
drawAnything(r)

1

    
    