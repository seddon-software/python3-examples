# you can transpose a matrix using zip
a = [[1,2,10], [3,4,20], [5,6,30]]
print zip(*a)

# you can wrap this up as a function
def unzip(x): 
    return zip(*x)

print unzip(a)