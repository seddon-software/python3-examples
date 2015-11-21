def isprime(n):
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

x = 2009
for n in range(20):
    if isprime(x): 
        print n, x
    else:
        print n
    x = x * 10 + 3 