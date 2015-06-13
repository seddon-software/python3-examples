import sys
sys.path.append('subdir')


import mypackage.mylib
from mypackage.mylib import MyClass as M
from mypackage.mylib import g1
import mypackage.mylib as mm

m = mypackage.mylib.MyClass()
m = M()
m.f1()
m.f2()
m.f3()
m.f4()
mm.g1()
mypackage.mylib.g2()
mypackage.mylib.g3()
mypackage.mylib.g4()
