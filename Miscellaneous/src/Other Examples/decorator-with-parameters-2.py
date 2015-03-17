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
def complexDecorator(mylambda, xx, yy, zz):
    def concreteDecorator(fn):
        def rotate(x, y, z):
            return fn(mylambda(y,yy), mylambda(z,zz), mylambda(x,xx))
        return rotate
    return concreteDecorator

@complexDecorator(lambda x,y:x+y,50,60,70)
def doit(a, b, c):
    print a, b, c


doit(5,6,7)



1
