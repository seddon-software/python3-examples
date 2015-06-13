import gc

class A(object):
    def __del__(self):
        print "DTOR"
 
for z in (1,):
    a = A()
    b = A()
#     a.x = b
#     b.x = a
#     del a
#     del b
gc.collect()
1