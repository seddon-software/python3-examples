import mylib as m

def f1():
    print "local f1"
from mylib import f2, f3, f4
from mylib import f1 as ff1

print m.__dict__
f1()
ff1()
m.f1()
f2()
f3()
f4()
