import numpy as np
np.set_printoptions(precision=3)

# start with a float64 array
matrix1 = np.fromfunction(lambda i,j: (i+2)*(j+2)**1.4, (4,4))
print matrix1.dtype, id(matrix1)
print matrix1

# casting creates a new array of int
matrix2 = matrix1.astype(int)
print matrix2.dtype, id(matrix2)
print matrix2

# casting creates a new array of bool
matrix3 = matrix1.astype(bool)
print matrix3.dtype, id(matrix3) 
print matrix3
