############################################################
#
#    callable classes as callbacks
#
############################################################

import sys


# create a callable class
class MyClass:
    def __call__(self, count):
        sum = 0
        for i in range (1, count):
            sum += i        

def doIt(iterations):
    m = MyClass()
    m(iterations)

doIt(int(sys.argv[1]))

1
