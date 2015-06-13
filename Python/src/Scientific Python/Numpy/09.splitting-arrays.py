############################################################
#
#    splitting arrays
#
############################################################

from numpy import *

a = array( random.random((3,5)) * 100 ); 
a = round_(a, 2)
print a

print "split horizontally"
a0,a1,a2,a3,a4 = hsplit(a,5)
print a2

print "split vertically"
a0,a1,a2 = vsplit(a,3)
print a
print a1

print "split unequal horizontally"
a0,a1,a2 = hsplit(a,(2,3))  # split at col 2 and 3
print a
print "a0 ="; print a0
print "a1 ="; print a1
print "a2 ="; print a2



1
