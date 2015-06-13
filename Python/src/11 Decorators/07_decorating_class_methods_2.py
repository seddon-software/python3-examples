############################################################
#
#    decorators
#
############################################################

def trace(fn):
    trace.f = lambda fn:fn
    def enhance(obj,value):
        print "calling obj.{0}({1})".format(fn.func_name, value)
        return fn(obj, value)
    return enhance
    
    
class MyClass(object):
    def trace2(fn):
        trace.f = lambda fn:fn
        def enhance(obj,value,fn=fn):
            print "--calling obj.{0}({1})".format(fn.func_name, value)
            return fn(obj, value)
        return enhance
    
    
    def __init__(self, a):
        self.a = a
    
    def bar(self, fn):
        return fn
        
    @trace
    def doitxxx(self):
        print 'doit'
    @trace.f
    def doit(self):
        print 'doit++'

    @trace
    def add(self, b): 
        print "result of add is: ", self.a + b
        
m = MyClass(100)
m.add(25)
trace(m.add(25))
trace(m.doit())
trace.f(m.doit())

1
