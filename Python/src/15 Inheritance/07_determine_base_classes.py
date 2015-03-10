class X : pass

class A : pass
class B : pass
class C(X) : pass

class MyClass(A,B,C): pass

m = MyClass()

# what is the class of an object
print m.__class__

# what are the immediate super classes
print MyClass.__bases__


1