############################################################
#
#    generator expressions
#
############################################################

from math import sqrt

# generator expressions are similar to comprehensions, except they
# evaluate each expression on demand (lazy evaluation), whereas comprehensions
# evaluate all expressions immediately

# use brackets to return a generator expression:
roots = (sqrt(x) for x in range(10))

# iterate using the generator
for r in roots:
    print "{0:6.2f}".format(r),
print


# comprehensions behave like generator expressions (but are evaluated immediately)
roots = [sqrt(x) for x in range(10)]
for r in roots:
    print "{0:6.2f}".format(r),
print


# a tuple is a generator, hence the syntax:
generator = (2,3,4,5)
for n in generator:
    print n,



# the following summation code will build a full list of squares in memory, iterate over those values, 
# and when the reference is no longer needed, delete the list:
print sum([x*x for x in range(10)]),

# memory is conserved by using a generator expression instead:
print sum(x*x for x in range(10))

1
