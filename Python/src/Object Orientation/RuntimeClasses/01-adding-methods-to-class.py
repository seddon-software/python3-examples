import types

class X: pass

def f(self): print "instance method f"

@staticmethod
def g(): print "class method g"

# add methods to class
X.f = f
X.g = g

# call methods
x1 = X()
x1.f()
X.g()

x2 = X()
x2.f()



class SpecialClass(object):
    @classmethod
    def removeVariable(cls, name):
        return delattr(cls, name)

    @classmethod
    def addMethod(cls, func):
        return setattr(cls, func.__name__, types.MethodType(func, cls))

def square(self, n):
    print n * n

instance = SpecialClass()
SpecialClass.addMethod(square)

SpecialClass.square(5)
instance.square(6)
SpecialClass.removeVariable("square")

# these calls will now fail
try:
    instance.square(7)
except:
    print "failed"
    
try:
    SpecialClass.square(8)
except:
    print "failed"

