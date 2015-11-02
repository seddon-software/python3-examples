cdef extern from "f.h":
    void f()
    
def say_hello():
    print "say_hello was compiled using cython"

def say_goodbye():
    print "say_goodbye was compiled using cython"

