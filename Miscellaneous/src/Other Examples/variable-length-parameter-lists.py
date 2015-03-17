############################################################
#
#    variable-length-parameter-lists
#
############################################################



def f(x,y,*args):
    print "x,y =", x, y
    print len(args), "additional args: ",
    
    for eachArg in args:
        print eachArg,
    print


f(3,4,10,20,30,40)
f(3,4,range(10,20))


