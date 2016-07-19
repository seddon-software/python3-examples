# you can transpose a matrix using zip
a = [[1,2,10], [3,4,20], [5,6,30]]
print((list(zip(*a))))

# you can wrap this up as a function
def unzip(x): 
    return list(zip(*x))

print((unzip(a)))