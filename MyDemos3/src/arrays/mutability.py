x = [ [10, 20], (30, 40) ]

try:
    x[1][1] = "this is a string"
except:
    print "can't do that"
    
print x

