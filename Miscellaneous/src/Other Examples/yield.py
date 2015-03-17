############################################################
#
#    yield.py
#
############################################################



# iterate over a collection
myIterator = iter([11,22,33])
for item in myIterator:
    print 'item:', item

# define your own iterator using yield
def getIterator(collection):
     i = iter(collection)
     for item in i:
         yield '<%s>' % item

collection = [111,222,333]
for x in getIterator(collection): 
    print x

1

