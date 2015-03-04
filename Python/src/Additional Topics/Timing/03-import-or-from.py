from timeit import timeit

# compare two ways of performing sqrt (1,000,000 iterations)
print "import", timeit('math.sqrt(50.0)','import math')
print "from  ", timeit('sqrt(50.0)','from math import sqrt')

# just do 10,000 iterations
print "import", timeit('math.sqrt(50.0)','import math', number=10*1000)
print "from  ", timeit('sqrt(50.0)','from math import sqrt', number=10*1000)

1
