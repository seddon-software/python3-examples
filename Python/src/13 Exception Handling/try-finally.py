############################################################
#
#    try-finally statements
#
############################################################

try:
    array = [1,2,3,4,5,6]
    
    try:
        for x in array:
            print array[x - 1],
    finally:
        print "... entering finally block"
    
    try:
        for x in array:
            print array[x * 2],
    finally:
        print "... entering finally block"

    print "CCC"
    print "DDD"
    
except Exception, e:
    print "Problems"
    
print "AAA"
print "BBB"


1