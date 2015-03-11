def f(x):
    y = x * x       # defines a local variable
    def inner():
        y = y * 2   # defines a new local variable (y) which shadows that defined in f
                    # hence the RHS of this expression refers to the local y which is undefined 
        return y
    return inner()

try:
    print f(5)
except UnboundLocalError, e:
    print e
    
1
