############################################################
#
#    decorators
#
############################################################

def DoubleIt(fn):
    def enhance(y):
        return fn(y) + fn(y)
    return enhance

def square(x): 
    return x * x

# this how we decorate without annotations
print DoubleIt(square)(10)

# this is how we decorate with annotations
@DoubleIt
def Square(x): 
    return x * x

print Square(10)

1
