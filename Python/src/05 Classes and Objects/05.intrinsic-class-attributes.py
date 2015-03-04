############################################################
#
#    intrinsic-class-attributes
#
############################################################

class Base:
    pass


class Derived(Base):
    "This is the Derived class"
    def Display(self):
        pass

    

print Derived.__name__
print Derived.__doc__
print Derived.__module__
print Derived.__dict__
print Derived.__bases__
print "================================="

x = Derived()
x.color = "red"
x.width = 10
print x.__class__
print x.__dict__
