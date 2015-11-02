"""
Modify the previous example to return the sum of the two 
input arrays instead of printing the result.
"""

def AddArrays(array1, array2):
    result = list(array1)

    for i, item in enumerate(result):
        result[i] += array2[i]
    
    return result


a1 = ( 3,  6,  9, 10, 20, 17, 14)
a2 = (17, 14, 11, 10,  0,  3,  6)
result = AddArrays(a1, a2)
print result

