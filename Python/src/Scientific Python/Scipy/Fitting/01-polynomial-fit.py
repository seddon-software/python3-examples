import numpy as np
import pylab as plt
from scipy.optimize import curve_fit

# define a square function with 3 unknowns: a, b and c
def square(n, a, b, c): 
    return a * n * n + b * n + c



X = np.array([1.00, 2.00, 3.00,  4.00,  5.00,  6.00])
Y = np.array([1.11, 5.04, 8.91, 17.03, 27.43, 35.03])
Y = 2 * Y
fitResults, b = curve_fit(square, X, Y)
results = "a = {:5.2f}\nb = {:5.2f}\nc = {:5.2f}\n".format(fitResults[0], fitResults[1], fitResults[2])

plt.xlabel("$x$", fontsize=24)
plt.ylabel("$x^2$", fontsize=24, labelpad=20, rotation=0)
plt.title("Least Squares Fit", fontsize=24)

# plot data
plt.plot(X, Y, 'ro')

# plot fitted curve
X = np.arange(0, 6, 0.01)
Y = [square(x, *fitResults) for x in X]
plt.plot(X, Y, color='blue', lw=2, label=results)
plt.legend(loc = 2)

plt.show()

