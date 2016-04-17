import sympy

x, y, z = sympy.symbols('x, y, z')
eq = x - x**2.5 + 7
z = sympy.solve( eq, x )

# note most of the results are complex (I represents sqrt(-1))
for result in z:
    print sympy.N(result, 5)    # N is used to limit precision
