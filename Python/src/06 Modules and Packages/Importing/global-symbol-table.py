############################################################
#
#    mypackage.py
#
############################################################

def trace():
    pass
x = 200
    
symbols = dict(globals())
for key, value in symbols.iteritems():
    print "{0:16} {1}".format(key, value)
    



