############################################################
#
#    raise statements
#
############################################################

array = [1,2,3,-4,5,6]

try:
    for x in array:
        if x < 0: 
            raise ValueError("array index is negative!")
        print x,
except ValueError, value:
    print
    print "... entering except block: " + str(value)


