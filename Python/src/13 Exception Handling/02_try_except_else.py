############################################################
#
#    try-except-else statements
#
############################################################

from math import sqrt
 
x = int(raw_input("Enter positive integer: "))

try:
    root = sqrt(x)
except:
    print "sqrt() failed ..."
else:
    print "sqrt() succeeded ..."
    print root
 

1
