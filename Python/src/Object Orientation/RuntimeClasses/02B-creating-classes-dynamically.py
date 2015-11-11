# new style classes
import types

class B(object): pass
class C(object): pass
print type(B)
print type(C)

# create a class from a string (determined at runtime) and 2 objects
A = type("A", (B, C), {'i':10, 'j':20, 'k':30})
a1 = A(); a1.__dict__ = {'x':101, 'y':201, 'z':301}
a2 = A(); a2.__dict__ = {'x':102, 'y':202, 'z':302}

# add 3 methods to class
A.f1 = types.MethodType(lambda self:"f1()", A)
A.f2 = types.MethodType(lambda self:"f2()", A)
A.f3 = types.MethodType(lambda self:"f3()", A)

# print info on class
print "base classes of A:", A.__bases__
print "class dictionary of A:", A.__dict__

# print info on objects
print "a1's class =", a1.__class__
print "a1's dictionary =", a1.__dict__
print "a2's class =", a1.__class__
print "a2's dictionary =", a1.__dict__

# call methods
for obj in [a1, a2]:
    print obj.f1()
    print obj.f2()
    print obj.f3()
    