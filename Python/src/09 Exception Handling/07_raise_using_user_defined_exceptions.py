############################################################
#
#    raise statements
#
############################################################

class MyException(Exception):
    def __init__(self, *args):
        Exception.__init__(self, args)

array = [1,2,3,-4,5,6]

try:
    for x in array:
        if x < 0: 
            raise MyException("array value is negative!", x)
        print(x, end=' ')
except MyException as e:
    print() 
    print("... entering finally block: ")
    print(e)


