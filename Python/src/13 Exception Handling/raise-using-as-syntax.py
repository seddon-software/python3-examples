############################################################
#
#    raise statements
#
############################################################


array = [1,2,3,-4,5,6]

try:
    for x in array:
        if x < 0: 
            raise Exception("array value is negative!")
        print x,
except Exception as e:
    print
    print "... entering finally block: "
    print e


