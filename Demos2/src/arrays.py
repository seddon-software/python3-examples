x = [ [10, 20], (30, 40) ]

try:
    x[1][0] = "abcdef"
    print "it worked!"
except:
    print "oops"
    
print x
# print x[0]
# print x[1]
# print x[1][0]
