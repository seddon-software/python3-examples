############################################################
#
#    binding functions to classes
#
############################################################

import types

# define a function
def f(self): print "calling f with", self.name

# define a class with no methods
class A(object): pass

# create objects
a1 = A(); a1.name = "a1"
a2 = A(); a2.name = "a2"
a3 = A(); a3.name = "a3"

# attempt simple binding
try:
    a1.f = f 
    a1.f(a1)    # works, but is awkward
    a1.f()      # fails
except Exception, e:
    print "***Error: Simple binding:", e
    
# use MethodType 
a1.f = types.MethodType(f, a1, A)   # bind f to an instance a1 of A
a1.f()

# check if f is bound to other objects
try:
    a2.f()
except Exception, e:
    print "***Error: Checking with a2:", e

# bind method to all objects in the class
A.f = f
# note that we don't need to create a method with types.MethodType here, 
# because all functions in the body of a class will become methods and 
# receive self, unless you explicit say it's a classmethod or staticmethod.

# check we can call bound methods
a1.f()
a2.f()
a3.f()



1