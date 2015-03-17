############################################################
#
#    variable-length-parameter-lists-2
#
############################################################



def f(x,y,**hash):
    print "x,y =", x, y
    print len(hash), "additional args: ", hash
    


f(3,4,mon=6,tue=7,wed=8)
f(3,mon=6,tue=7,wed=8, y=4)


