square = lambda x : x**2
cube = lambda x : x**3
quad = lambda x : x**4

print( square(8) )
print( cube(7) )
print( quad(6) )

def power(fn, n):
    return fn(n)

# 4000 lines of code in here

print( power(quad, 5))
print( power(lambda x : x**5, 5))

average = (
                  lambda x, y, z : 
            (square(x) + y + z)/3
        )
print(average(3, 5, 7))