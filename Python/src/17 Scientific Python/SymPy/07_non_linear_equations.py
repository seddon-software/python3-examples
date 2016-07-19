import sympy
import pylab as plt

x, y, z = sympy.symbols('x, y, z')
eq = x - x**2.5 + 7
z = sympy.solve( eq, x )

# note most of the results are complex (I represents sqrt(-1))
for result in z:
    print sympy.N(result, 5)    # N is used to limit precision


# show the graph
X = plt.arange(-5, 5, 0.01)

Y = X - X**2.5 + 7
plt.plot(X, Y, color='red', lw=2)

Y = X*0
plt.plot(X, Y, color='blue', lw=1)

plt.axhline(0, color='blue')
plt.axvline(0, color='blue')

plt.show()
