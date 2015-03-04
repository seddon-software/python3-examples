# timeit.timeit(stmt[, setup[, timer[, number=1000000]]])
#
#  Create a Timer instance with the given statement, 
#  setup code and timer function and run its timeit() method with number executions.

from timeit import timeit
count = 1

print "using xrange", timeit("sum(xrange(100000000))", number = count)
print "using range", timeit("sum(range(100000000))", number = count)

print "using xrange", timeit("for x in xrange(10 * 1000 * 1000): total = total + x",
                             'total = 0', number = count)
print "using range ", timeit('for x in range(10 * 1000 * 1000): total = total + x', 
                             'total = 0', number = count)


1
