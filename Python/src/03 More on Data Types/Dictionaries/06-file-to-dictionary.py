############################################################
#
#    sorting-dictionaries
#
############################################################

# dictionaries can't be sorted, but we can print out
# key value pairs in lexical order

# 1. Read in dictionary from file
phones = {}
try:
    f = open("data/codes.txt", "r")
    for line in f:
        list = line.rstrip().split(' ')
        value = list[0]
        key = " ".join(list[1:])
        phones[key] = value
except IOError, e:
    print "Reading data from file failed!"
    print e
finally: 
    f.close()

# 2. Sort the keys

sortedKeys = phones.keys()
sortedKeys.sort()

# 3. Iterate through sorted list
for key in sortedKeys:
    print key + ":" + phones[key]
    
