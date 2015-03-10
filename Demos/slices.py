import copy

list1 = range(10,20)
list2 = range(30,35)
print list2
list2[1:4:2] = list1[3:4]
print list2
