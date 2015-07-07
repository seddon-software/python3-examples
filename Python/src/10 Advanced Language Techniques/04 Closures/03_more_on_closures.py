# Closures close over variables, not values

############################################################
# Part 1 - closure fails
def outer():
    x = 50
    def inner():
        print inner.__closure__
        x += 1  # x refers to local x => NO closure
        print "locals for inner(): ", locals()        
    return inner

def test():
    f = outer()
    try:
        print "locals for test(): ", locals()        
        f()     # outer 'x' is not in scope here
                # hence exception raised
    except UnboundLocalError, e:
        print e

test()
print

############################################################
# Part 2 - workaround for the above problem

def outer():
    x = [50]     # x is mutable
    def inner():
        print "locals for inner(): ", locals()        
        print inner.__closure__
        print "Cell contents: ", inner.__closure__[1].cell_contents
        x[0] += 1  # x refers to outer 'x' because its mutable => closure
        print "x[0] = ", x[0]
    return inner

def test():
    f = outer()
    try:
        f()     # outer 'x' is brought into scope by the closure
                # hence NO exception raised
    except UnboundLocalError, e:
        print e

test()
print "finished"
