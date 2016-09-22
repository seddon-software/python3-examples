def trace(fn):
    def inner(n):
        print("calling {}({})".format(fn.__name__, n))
        return fn(n)
    return inner
    
@trace
def square(n):
    return n**2

@trace
def cube(n):
    return n**3

# print( trace(square)(7) )
# print( trace(cube)(8) )
print( square(7) )
print( cube(8) )


