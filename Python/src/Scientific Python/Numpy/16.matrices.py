############################################################
#
#    matrices
#
############################################################

from numpy import *

# matrix multiplication (not element wise multiplication)
a = matrix( [[3,4,5],[2,3,8],[4,1,7]] ); print a
b = matrix( [[2,3,4],[1,2,7],[3,0,6]] ); print b
c = a * b; print c

a = matrix( [[3,5],[4,1]] ); print a
print "Transpose"; print a.T
print "Inverse"; print a.I
print "Determinate", linalg.det(a)
# linear algebra
# 5x + 3y = 31
# 2x - 7y = -45
# solution x=2, y=7
a = matrix( [[5,3],[2,-7]] )
v = matrix( [[31],[-45]] )
print linalg.solve(a,v)

1

