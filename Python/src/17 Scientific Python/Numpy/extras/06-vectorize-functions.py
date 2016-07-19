import numpy as np
np.set_printoptions(precision=3)

# this only wors for scalars
def square(x): return x * x

# vectorize function to return floats
Square = np.vectorize(square, otypes=[np.float])
X = np.arange(5, 10)
print Square(X)         # now works for vectors
print Square(10)        # but still works for scalars

