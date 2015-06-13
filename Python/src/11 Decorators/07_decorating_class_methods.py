############################################################
#
#    decorators
#
############################################################

def trace(fn):
    def enhance(obj,value):
        print "calling obj.{0}({1})".format(fn.func_name, value)
        return fn(obj, value)
    return enhance
    
    
class MyClass(object):
    def __init__(self, a):
        self.a = a
        
    @trace
    def add(self, b): 
        print "result of add is: ", self.a + b
        
m = MyClass(100)
m.add(25)
# currying version
trace(m.add(25))

1
