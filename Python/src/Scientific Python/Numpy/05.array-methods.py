############################################################
#
#    array methods
#
############################################################

from numpy import *

a = array( random.random(10) * 100, dtype="int" )
print a
print type(a)

print "sum=", a.sum()
print "max=", a.max()
print "min=", a.min()

# perform operations along specified axis
a = arange(12).reshape(3,4)
print a
print a.sum(axis=0)
print a.sum(axis=1)

1
