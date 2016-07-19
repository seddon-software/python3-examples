############################################################
#
#    using-mro
#
############################################################

o = object
class A(o):
    def __init__(self,**kwargs):
        super(A,self).__init__()
        self.a = kwargs['a']

class B(A):
    def __init__(self,**kwargs):
        super(B,self).__init__(**kwargs)
        self.b = kwargs['b']

class C(A):
    def __init__(self,**kwargs):
        super(C,self).__init__(**kwargs)
        self.c = kwargs['c']

class D(B,C):
    def __init__(self,**kwargs):
        super(D,self).__init__(**kwargs)
        self.d = kwargs['d']

myObject = D(a=1,b=2,c=3,d=4)


1
    

