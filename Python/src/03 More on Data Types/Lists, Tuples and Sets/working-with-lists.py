############################################################
#
#    working-with-lists
#
############################################################

list1 = [[1,2],[3,4]]

# notation for accessing lists
print list1
print list1[1]
print list1[1][0]

# modifying lists
list1[1][0] = 99
print list1[1][0]

# append and extend are equivalent
list2 = [10, 20, 30]
list = []
list.extend(list1)
list.append(list2)
print list

# lists can contain tuples
list3 = [tuple((1,2)), tuple((3,4)), tuple((5,6))]
print list3

