# * packs parameters into a tuple
def average(*a):   # variadic function
    sum = 0.0
    for item in a:
        sum += item
    return sum / len(a)

print average(7, 8)
print average(7, 8, 10, 12, 34, 44, 87)
x = [ 7, 8, 10, 12, 34, 44, 87 ]
# * unpacks parameters from list or tuple
print average(*x)

