def doit(a):
    def square(x):
        return x**2
    def cube(x):
        return x**3
    doit.this = square
    y = square(a) + cube(a)
    print( locals() )
    return y
print( doit(5) )
print( doit.__dict__ )
print( doit.this(5) )
