############################# immutable

def incr(x):
    x = x + 1
    return x

a = 100
print id(a)
a = incr(a)
print a
print id(a)

############################### mutable

def addItem(mylist):
    mylist.append(99)

a = [4,5,6]
addItem(a)
print a




