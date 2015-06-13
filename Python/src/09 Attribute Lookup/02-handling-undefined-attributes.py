############################################################
#
#    handling undefined attributes
#
############################################################

# replacing failed lookup with a method call
def MissingMethods():
    class MyClass(object):
        def __getattr__(self, attr):
            self.missingAttribute = str(attr)
            return self.replacement  # this method gets called instead
        
        def replacement(self): 
            print "attribute '{0}' not found".format(self.missingAttribute)
        def f(self): print "f()"
        def g(self): print "g()"
        def h(self): print "h()"
    
    # __getattr__ only called if lookup fals
    o = MyClass()
    o.f()
    o.g();
    o.h();
    o.dummy()

# replacing failed lookup with data
def MissingData():
    class MyClass(object):
        def __init__(self):
            self.data = {'a':100, 'b':200, 'c':300}
            self.x = 10
            self.y = 20
            self.z = 30
            
        def __getattr__(self, attr):
            return self.data[attr]
        
    o = MyClass()
    print o.x
    print o.y
    print o.z
    print o.a
    print o.b
    print o.c


MissingData()
MissingMethods()
    
1