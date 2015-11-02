import numpy as np


matrix = np.fromfunction(lambda i,j: 10*i+j, (10,10), dtype = int)
print "matrix=\n", matrix

row_indices = [4, 5, 6]
print "row_indices:\n", matrix[row_indices]

col_indices = [3, 4, 5]
print "col_indices:\n", matrix[:,col_indices]

indices = [0, 11, 22, 33, 44, 55]   # array is treated as 1 dimensional
print "take:\n", matrix.take(indices)
print "take:\n", np.take(matrix, indices)

indices = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4]   # choose selects from 5th of row 0, 4th of row 1 ...
print "choose:\n", np.choose(indices, matrix)

diagonal = range(-1, -11, -1)
print "matrix=\n", matrix
print "row and col indices:\n", matrix[diagonal, diagonal]
print "diag:\n", np.diag(matrix)
print "diag with offset:\n", np.diag(matrix, -3)

