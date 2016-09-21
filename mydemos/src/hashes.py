import sys
import pprint
pprint.pprint(sys.path)
salary = {
           'Tom' : 34000,
           'Sue' : 76000,
           'Jim' : 47000,
           'Ali' : 50000,
           'Bill': 47000
         }
k = salary.keys()
l = list(salary.keys())
print(k)
print(l)

#salary['Tom'] = 35000
salary['Peter'] = 65000
print(k)
print(l)
# salary['Jim'] = None
# #salary.pop('Bill')
# del salary['Bill']
# print(salary)
