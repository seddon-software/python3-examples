############################################################
#
#    broadcasting
#
############################################################

from numpy import *

a = [2, 4, 6, 8, 10]
x = hstack(a); print x
y = vstack(a); print y

f = x * y

print f

1
