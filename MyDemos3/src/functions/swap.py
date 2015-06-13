mylist = [ 2, 4, 6]
mylist2 = [x, y, z] = mylist 
print x, y, z
print mylist2

def swap(a, b):
    return b, a


x = 100
y = 200
x, y = swap(x, y)
print x, y

x, y = y, x 
print x, y