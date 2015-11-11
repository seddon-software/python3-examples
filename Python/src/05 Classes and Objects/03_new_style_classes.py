# old style classes do NOT derive from the object class

class A(): pass
class B(): pass
print type(A)
print type(B)

# new style classes DO derive from the object class

class C(object): pass
class D(object): pass
print type(C)
print type(D)
