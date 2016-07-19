import numpy as np
x = np.array([1, 2, 3], dtype=np.int32)
print str(x.__array_interface__)      

for key, value in x.__array_interface__.iteritems():
    print key, value

