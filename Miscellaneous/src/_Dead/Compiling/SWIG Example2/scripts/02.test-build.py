import sys
sys.path.append("../src/build/lib.win32-2.7")
sys.path.append("../src")

from _example import *
from example import *
iv = IntVector(4)         # Create an vector<int>
for i in range(0,4):
    iv[i] = i
print average(iv)
      
