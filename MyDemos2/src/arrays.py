import copy
x = [ [10, 20], [30, 40], [50, 60], [70, 80], [90, 100] ]



y = x[:]    # copy
z = copy.deepcopy(x)       
print(id(x), id(x[3]))
print(id(y), id(y[3]))
print(id(z), id(z[3]))
print(x)
print(y)
print(z)
