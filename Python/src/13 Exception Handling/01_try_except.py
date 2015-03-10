############################################################
#
#    try-except statements
#
############################################################

array = [1,2,3,4,5,6]

try:
    for x in array:
        print x, array[x]
        print "A"
        print "B"
except IndexError,mytarget:
    print "... entering except block"
    print mytarget


1
