"""
Write a function that takes two int arrays (same size) 
as parameters and adds the arrays together, element by 
element.  Print out the array as part of the function.
"""

def AddArrays(array1, array2):
    for i, item in enumerate(array1):
        print array1[i] + array2[i],


a1 = ( 3,  6,  9, 10, 20, 17, 14)
a2 = (17, 14, 11, 10,  0,  3,  6)

AddArrays(a1, a2)
