class MyClass:
    # must have a method to start with
    def f(self, x): pass
    
m = MyClass ()


# implement new methods
def instance_method (self):
    print "instance_method"

def class_method (self):
    print "class_method"

# attach method to object (bound)
attach = type(MyClass.f)    # doesn't have to be called attach
m.g = attach(instance_method, m, MyClass)
print "object dict:", m.__dict__

# attach method to class (unbound)
MyClass.h = attach(class_method, None, MyClass)
print "class dict:", MyClass.__dict__
print

# check we can call methods through m
m.h()   # h() is in the class dictionary
m.g()   # g() is in the m's dictionary

# try calling methods through another object
x = MyClass()
x.h()   # h() is in the class dictionary
try:
    x.g()   # g() is in the m's dictionary, so this fals
except Exception, e:
    print e

