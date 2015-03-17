import sys
sys.path.append("../src/build/lib.win32-2.7")
sys.path.append("../src")

import _myexample
_myexample.say_hello("World")
_myexample.say_goodbye("Universe")

import myexample


iv = myexample.IntVector(4)
dv = myexample.DoubleVector(7)

for i in range(0,4):
    iv[i] = i * 100    
print myexample.average(iv)

for i in range(0,7):
    dv[i] = float(i * 100)    
print myexample.average2(dv)
