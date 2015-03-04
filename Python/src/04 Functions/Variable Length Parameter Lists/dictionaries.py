############################################################
#
#    Variable Length Parameter Lists
#
############################################################

def f(x,y, **params):
    print 'x,y:', x, y
    print 'params:', params
    print params['May']
    

hash = { 'a':1, 'b':2 }    
f(13,7, May=5, Jan=1, Feb=2, Dec=12, **hash)
f(13,7, Jan=1, Feb=2, Dec=12, **hash)


