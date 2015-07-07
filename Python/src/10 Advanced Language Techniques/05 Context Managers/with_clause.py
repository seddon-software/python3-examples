############################################################
#
#    with clause
#
############################################################

import sys


class MyClass:
    def __enter__(self):
        print "WITH: initialization"
        return self # object to be used in with clause
    
    def __exit__(self, type, value, traceback):
        print "WITH: cleanup"
        print "type:     ", type
        print "value:    ", value
        print "traceback:", traceback
        if isinstance(value, Exception):
            return True   # suppress Expression
        else:
            return False

    def hello(self):
        print "Hello",

    def oops(self):
        raise Exception("oops")

print "============ WITH =========================="        
with MyClass() as m:
    m.hello()
    m.oops()


print "============ Equivalent Code ==============="        
try:
    m = MyClass().__enter__()
    m.hello()
    m.oops()
except Exception, e:
    traceback = sys.exc_info()
    m.__exit__(type(e), e, traceback[-1])
else:
    m.__exit__(None, None, None)


