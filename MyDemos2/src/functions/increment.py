def addOne(n):
    n = n + 1
    return n

x = 100
x = addOne(x)
print x

mylist = [2, 4, 6, 8]
def addOneToList(n):
    n.append(99)

addOneToList(mylist)
print mylist
