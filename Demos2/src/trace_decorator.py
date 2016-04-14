def trace(fn):
    def enhance(n):
        print "calling {} with {}".format(fn.__name__, n)
        return fn(n)
    return enhance
    
@trace    
def square(n): 
    return n * n
@trace
def cube(n): 
    return n ** 3

print square(5)
print cube(5)
# print trace(square)(5)
# print trace(cube)(5)
