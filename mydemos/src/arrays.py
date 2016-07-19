import copy
x = [ [10, 20], [30, 40], [50, 60], [70, 80], [90, 100] ]
y = x[:]    # shallow copy
z = copy.deepcopy(x)
t = list(x)  # cast (shallow copy)
print(t)
print(id(x), id(x[0]), id(x[1]))
print(id(y), id(y[0]), id(y[1]))
print(id(z), id(z[0]), id(z[1]))
print(id(t), id(t[0]), id(t[1]))


