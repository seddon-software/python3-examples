############################################################
#
#    reduce
#
############################################################

# Greatest Common Divisor of two numbers
gcd = lambda a, b : a if b == 0 else gcd(b, a % b)
                                       
# Lowest Common Multiple of two numbers
lcm = lambda a, b : a * b // gcd(a, b)

# Lowest Common Multiple of several numbers
lcmm = lambda *args : reduce(lcm, args)

print gcd(15, 35)
print lcm(10, 15)
print lcmm(10, 15, 20)
print lcmm(10, 15, 20, 25)



1
