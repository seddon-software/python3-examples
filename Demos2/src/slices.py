import copy

x = [ [10, 20], [30, 40] ]
y = x[:][:]
z = x


print y
print id(x[0]), id(y[0]), id(z[0])
print id(x[1]), id(y[1]), id(z[1])





