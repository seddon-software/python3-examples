############################################################
#
#    broadcasting
#
############################################################

import numpy as np

a = [2, 4, 6, 8, 10]
x = np.hstack(a); print x
y = np.vstack(a); print y

f = x * y

print f

1
