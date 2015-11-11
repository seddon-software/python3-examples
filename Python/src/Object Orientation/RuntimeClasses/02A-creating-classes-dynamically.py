import new  # this works with old stle classes (not derived from object)
            # new module is replaced by types module in Python 3

# must be old style classes
class B: pass
class C: pass
print type(B)
print type(C)

# create a class from a string (determined at runtime) and 2 objects
A = new.classobj("A", (B, C), {'i':10, 'j':20, 'k':30})
a1 = new.instance(A, {'x':101, 'y':201, 'z':301})
a2 = new.instance(A, {'x':102, 'y':202, 'z':302})

# add 3 methods to class
A.f1 = new.instancemethod(lambda self:"f1()", None, A)
A.f2 = new.instancemethod(lambda self:"f2()", None, A)
A.f3 = new.instancemethod(lambda self:"f3()", None, A)

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
    