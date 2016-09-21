import lib as l
from lib import f2, f3, f4
from lib import f1 as ff1, f2 as ff2

print(l.__dict__)
l.f1()
l.f2()
l.f3()
l.f4()
def f1():
    print("local f1")
f1()
ff1()
f2()
f3()
f4()
