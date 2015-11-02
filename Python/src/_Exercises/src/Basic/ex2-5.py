"""
Write a program that calculates the ratio of successive 
pairs of the first 20 Fibonacci numbers.  Does the ratio 
appear to converge to a number?
"""

a, b = 0, 1

for n in range(20):
    print float(a)/b 
    a, b = b, a+b
    
