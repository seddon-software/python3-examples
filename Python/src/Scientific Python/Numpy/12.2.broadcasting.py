############################################################
#
#    broadcasting
#
############################################################

from numpy import *

# show dimensions
a = array([2,5,4]); print a.shape
z = zeros(9, dtype=int).reshape(3,3); print z.shape
print a
print z
# the + will expand the smaller array (broadcasting)
c = a + z; print c

b = array([[2,5,4],[8,7,3],[1,2,9]]); print b.shape
# in the calculation
# 1) a is already of shape (1,3)
# 2) broadcasting expands a to shape (3,3)
c = a + b; print c

# different dimensions
a = array([100,200,300,400]); print a.shape
b = arange(16).reshape(4,4); print b.shape
# in the calculation
# 1) a is converted to shape (1,4)
# 2) broadcasting expands a to shape (4,4)
c = a + b; print c    # 

a = ones( (3,3,3) ) * 5; print a.shape
print a
b = ones( (3,3) ) * 4; print b.shape
print b
c = a + b; print c


1
