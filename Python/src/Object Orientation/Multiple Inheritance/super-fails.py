############################################################
#
#    using-mro
#
############################################################

# this MI hierarchy doesn't work
# because super() doesn't behave as in Java
# ... it calls the next method in the MRO!!

class A(object):
    def __init__(self,x):
        super(A,self).__init__(x)

class B(object):
    def __init__(self,y):
        super(B,self).__init__(y)

class C(A,B):
    # mro = CABO
    # so A's super is B (not object!)
    def __init__(self,x,y):
        A.__init__(x)   # can't call CTOR without an object (unbound)
        B.__init__(y)
        

x = C(10,20)
    

1
