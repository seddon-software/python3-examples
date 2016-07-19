import numpy as np


matrix = np.fromfunction(lambda i,j: (i+2)*(j+2), (4,4))
print matrix, "\n"

# overwrite row 2
matrix[2,] = 99
print matrix, "\n"

# overwrite col 2
matrix[:,2] = 77
print matrix, "\n"
