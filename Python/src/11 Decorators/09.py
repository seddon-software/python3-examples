############################################################
#
#    decorators
#
############################################################

# this how we decorate without annotations

def f1(fn):
    print "f1",
    return fn

def f2(fn):
    print "f2",
    return fn

def f3(fn):
    print "f3",
    return fn

def f(x): 
    return x * x

print f1(f2)(f3)(f)(5)

# this is how we decorate with annotations

def g1(fn):
    print "g1",
    return fn

@g1
def g2(fn):
    print "g2",
    return fn

@g2
def g3(fn):
    print "g3",
    return fn

@g3
def g(x): 
    return x * x

print g(5)

1
