from __future__ import print_function
from math import *

def f(x):
    a = reduce(lambda x, y: x+y, range(1, x))
    return a
    
    
def output(A):
    for a in A:
        print("{0:8d}".format(a), end=' ')
    print()
    
N = [n for n in range(2,999)]
F = [f(n) for n in range(2,999)]
output(N)
output(F)

Z = [i+2 for i,f in enumerate(F) if f == 0]
print(Z)

print( [Z[i]-Z[i-1] for i,z in enumerate(Z)] )

 
