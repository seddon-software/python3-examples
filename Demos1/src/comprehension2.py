# 4 types of comprehension

# list comprehension
print [x**2 for x in range(10)]

# generator comprehension
for result in (x**2 for x in range(10)):
    print result,
print

# set comprehension
print {x**2 for x in (2, 3, 7, 4, 3, 7, 3, 2) if x > 3}

# dict comprehension
print {x:x**2 for x in (2, 3, 7, 4, 3, 7, 3, 2)}
