############################################################
#
#    Exception in destructor
#
############################################################

class MyClass(object):
    def __del__(self):
        raise Exception("Oops") # ignored
        print "Bar: Bye"

try:
    x = MyClass()
    raise Exception("only get here if exceptions ignored in DTOR")
except Exception, e:
    print e