############################################################
#
#    using-mro
#
############################################################

# this MI hierarchy doesn't work
# because super() doesn't behave as in Java
# ... it calls the next method in the MRO!!

class A(object):
    def __init__(self, x):
        self.x = x
        super(A,self).__init__()

class B(object):
    def __init__(self, y):
        self.y = y
        super(B,self).__init__()

class C(A,B):
    # mro = CABO
    # so A's super is B (not object!)
    def __init__(self, x, y):
        A.__init__(self, x)
        B.__init__(self, y)
        
a = A(10)
b = B(20)
x = C(10,20)
    

1
