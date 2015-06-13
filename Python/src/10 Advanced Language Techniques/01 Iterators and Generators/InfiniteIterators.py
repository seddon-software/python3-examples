from itertools import *


# these functions return infinite iterators
# once called they iterate forever

iter = count(10)
print iter.next()
print iter.next()
print iter.next()
print iter.next()
print iter.next()
print iter.next()

iter = cycle('ABCD')
print iter.next()
print iter.next()
print iter.next()
print iter.next()
print iter.next()
print iter.next()

# this only iterates 3 times
iter = repeat(10, 3)
print iter.next()
print iter.next()
print iter.next()
print iter.next()   # this fails
