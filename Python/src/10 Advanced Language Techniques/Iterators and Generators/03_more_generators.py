############################################################
#
#    generators
#
############################################################

# functions that contain yield can produce an iterable
def ids():
    for n in [2,3,5,7,11,13,17,19]: 
        yield n
    return

# calling the function produces an iterator
for n in ids():
    print n
    
