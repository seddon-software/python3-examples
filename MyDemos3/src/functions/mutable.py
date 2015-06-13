def addOne(x):
    x = x + 1
    return x    # immutable, so return a copy of pointer


a = 100
a = addOne(a)   # reset a with return value
print a

####################################

def addItem(x):
    x.append(99) # mutable, so no return necessary


a = [2, 3, 5, 7, 11]
addItem(a)     # no reset of pointer required
print a
