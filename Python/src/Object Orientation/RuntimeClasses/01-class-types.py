class A: pass
class B(object):pass
class C(A, B): pass
    
# determine type of old style class
print "type of A(old):", type(A)

# determine type of new style class
print "type of B(new):", type(B)

# determine type of mixed derived class
print "type of C(mixed):", type(C)
