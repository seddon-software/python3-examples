import copy
a = range(20, 35)
b = range(10, 15)
a[9:12:2] = b[2:5:2]
print a, len(a)
print b, b.__len__()




b = tuple(a)
c = list(a) # shallow copy
d = a[:]    # shallow copy
print id(a), id(d)

e = copy.copy(a)   # shallow copy
f = copy.deepcopy(a) 


