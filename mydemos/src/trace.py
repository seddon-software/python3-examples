def trace(fn):
    def jason(n):
        print("calling {}({})".format(fn.__name__, n))
        return fn(n)
    return jason

@trace
def square(n):
    return n**2
@trace
def cube(n):
    return n**3

# print( trace(square)(5) )
# print( trace(cube)(7) )
print( square(5) )
print( cube(7) )

