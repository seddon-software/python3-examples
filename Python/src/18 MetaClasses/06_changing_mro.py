############################################################
#
#    mro
#
############################################################

class MyMetaclass(type):
    # override the usual MRO defined by inheritance
    def mro(cls):
        return (cls, B, object) # note that A is missing
    
class A(object):
    def f(self): print "f()"

class B(A):
    def g(self): print "calling g() ..."

class C(B):
    __metaclass__ = MyMetaclass
    def h(self): print "calling h() ..."

print C.mro()
print C.__mro__
o = C();
o.h()
o.g()
try:
    o.f()   # this fails because A is not in the MRO for class C
except AttributeError, e:
    print e

1