# immutable data
def addOne(x):
    x = x + 1
    return x

a = 200
a = addOne(a)
print(a)

#########
# mutable data
def append99(l):
    l.append(99)

a = [3, 6, 4, 9]
append99(a)
print(a)
