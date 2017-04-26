def trace(fn):
    def fred(x):
        print('calling {}({})'.format(fn.__name__, x))
        return fn(x)
    return fred

@trace
def square(x):
    return x**2

@trace
def cube(x):
    return x**3

@trace
def quad(x):
    return x**4

print( quad(7) )
# print( trace(quad)(7) )

