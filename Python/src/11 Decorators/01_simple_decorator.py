############################################################
#
#    decorators
#
############################################################

def myDecorate(fn):
    def enhance(y):
        return fn(y + y)
    return enhance

def f(x): 
    return x * x

# this how we decorate without annotations
print myDecorate(f)(5)

# this is how we decorate with annotations
@myDecorate
def g(x): 
    return x * x

print g(5)

1
