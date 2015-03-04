############################################################
#
#    closures
#
############################################################

# define a closure containing width and precision
def printWithPrecision(width, precision):
    def printIt(x):
        format = "%" + str(width) + "." + str(precision) + "f"
        print format % x
    return printIt

print10dot3 = printWithPrecision(10, 3)
print8dot2 = printWithPrecision(8, 2)
print7dot1 = printWithPrecision(7, 1)

x = 1234.56789
y = 9876.54321
print "%10.3f" % x
print10dot3(x)
print10dot3(y)
print8dot2(x)
print8dot2(y)
print7dot1(x)
print7dot1(y)
1
