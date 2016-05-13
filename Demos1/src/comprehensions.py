from time import sleep

a = [ x**2 for x in (2, 3, 5, 7, 11, 13) if x > 4 ]  # list comprehension
print a

p = [sleep(1), sleep(3), sleep(5)]
q = (sleep(1), sleep(3), sleep(5))





b = [sleep(t) for t in (1, 3, 5)]
print "eager evaluation - list comprehension"

b = (sleep(t) for t in (1, 3, 5))
print "lazy evaluation - generator comprehension"
b.next()
b.next()
