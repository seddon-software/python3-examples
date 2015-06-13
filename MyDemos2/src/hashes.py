salary = { 'Sue' : 60000, 
           'Joe' : 45000, 
           'Jim' : 52000,
           'Ian' : 37000,
           'Kit' : 67000 
         }
# get the keys
sortedKeys = salary.keys()
sortedKeys.sort()

# sort the keys
# iterate over the sorted keys
for key in sortedKeys:
    print key, salary[key]
    
1
