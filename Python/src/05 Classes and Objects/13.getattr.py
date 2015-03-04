class A:
    def __init__(self, x):
        self.x = x

class B:
    def __init__(self, x):
        self.x = x
        
    def __getattr__(self, attr):
        return "__getattr__: no attribute called " + attr

a = A(100)
b = B(200)
print a.x
print b.x
print b.y

try:
    print a.y
except AttributeError, e:
    print "AttributeError exception:", e
    