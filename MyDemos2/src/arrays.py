p = [ [10, 20], (30, 40) ]

print p
print p[1]
print p[0][1]
print p[1][1]

try:
    p[1][1] = "hello"
except:
    print "Can't do that!"
print p


