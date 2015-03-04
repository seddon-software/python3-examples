############################################################
#
#    default parameters
#
############################################################

    
def Display(a, b=10, c=100):
    print "a = {0:6.2f}, b = {1:6.2f}, c = {2:6.2f}".format(a, b, c)


x = 100
y = 200
print "x and y are: {0:08} ---- {1} ".format(x, y)

Display(a=19, b=-6.2, c=4.8)
Display(b=-6.2, c=4.8, a=19 )
Display(17)
Display(17, 21)
Display(17, c=0)
