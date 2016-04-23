############################################################
#
#    main.py
#
############################################################

import sys
print sys.path
sys.path.append("mylib")

from package1.package2.ModuleA import A
from package1.package2.ModuleBC import B
from package1.package2.ModuleBC import C as CCC
from package1.package2 import help

help()
print A.__dict__
a = A()
b = B()
c = CCC()

a.f()
a.g()
a.h()

b.f()
b.g()
b.h()

c.f()
c.g()
c.h()
