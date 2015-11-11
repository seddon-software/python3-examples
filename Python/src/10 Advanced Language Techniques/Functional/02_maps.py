############################################################
#
#    maps
#
############################################################

from math import sqrt

def cube(x):
    return x * x * x


# set up a sequence
sequence = range(1, 20)

# apply a map to entire sequence
roots = map(sqrt, sequence)
for value in roots:
    print "%6.2f" % value, 
print

cubes = map(cube, sequence)
for value in cubes:
    print "%6i" % value, 
print

1
