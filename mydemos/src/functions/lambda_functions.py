def square(x):
    return x**2

def cube(x):
    return x**3

def quad(x):
    return x**4

def power(fn, x):
    return fn(x)

print( power(quad, 4) )
print( power(cube, 7) )
n = 6
print( power(lambda x:x**n, 10))
