############################################################
#
#    try-finally statements
#
############################################################

try:
    array = [1,2,3,4,5,6]
    
    try:
        for x in array:
            print(array[x - 1], end=' ')
    finally:
        print("... entering finally block")
    
    try:
        for x in array:
            print(array[x * 2], end=' ')
    finally:
        print("... entering finally block")

    print("CCC")
    print("DDD")
    
except Exception as e:
    print("Problems")
    
print("AAA")
print("BBB")


1