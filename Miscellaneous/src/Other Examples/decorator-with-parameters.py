############################################################
#
#    decorators
#
############################################################


# simple decorator
def concreteDecorator(fn):
    def rotate(x, y, z):
        return fn(y, z, x)
    return rotate

@concreteDecorator
def doit(a, b, c):
    print a, b, c
        
doit(5,6,7)


# complex decorator (has parameters)
def complexDecorator(xx, yy, zz):
    def concreteDecorator(fn):
        def rotate(x, y, z):
            return fn(y + yy, z + zz, x + xx)
        return rotate
    return concreteDecorator

@complexDecorator(50,60,70)
def doit(a, b, c):
    print a, b, c


doit(5,6,7)



1
