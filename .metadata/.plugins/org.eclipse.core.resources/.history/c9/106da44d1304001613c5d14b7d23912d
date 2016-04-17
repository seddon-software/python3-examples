from sympy import sqrt, diff
import sympy

def phi (x, y, sigma):
    return sqrt(x**2 + y**2 + sigma**2)


x, y, sigma = sympy.symbols('x, y, sigma')

# we are working with the function:
#  f(x, y, sigma) = (x**2 + y**2 + sigma**2)**0.5
#
#  => df/dx = 0.5*(x**2 + y**2 + sigma**2)**-0.5 * 2*x 
#           = x / (x**2 + y**2 + sigma**2)**0.5

# define the differential (dfdx):
r = sqrt(x**2 + y**2)
dfdx = x / sqrt(r**2 + sigma**2)

# now use sympy to calculate the differential
print diff(phi(x, y, sigma), x)             # looks different from dfdx
print dfdx - diff(phi(x, y, sigma), x)      # but difference is zero!
                                            # so it is correct