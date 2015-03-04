"""
Write a program that calculates the factorial of an integer 
in the range 2 to 10.  Add exception handling code to prevent 
calculating a result where the input number is larger than 10, 
or any negative integer.  Make sure you can handle the case 
where the input is not an integer.
"""

try:
    x = int(raw_input("Enter an integer for factorial calculation: "))
    if x > 10: raise Exception("number too large: " + str(x))
    if x <  2: raise Exception("number too small: " + str(x))
except Exception, e:
    print e
    exit(1)

result = 1
for i in range(1, x+1):
    result = result * i
    
print "Factorial of ", x, "= ", result


1