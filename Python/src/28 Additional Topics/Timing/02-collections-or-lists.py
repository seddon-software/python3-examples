from timeit import timeit

# timeit.timeit(stmt, setup, timer, number=??)
count = 100
print "collections", timeit('s.appendleft(100)', 'import collections; s = collections.deque()', number=count)
print "lists      ", timeit('s.insert(0,100)', 's = []', number=count)

count = 1000
print "collections", timeit('s.appendleft(100)', 'import collections; s = collections.deque()', number=count)
print "lists      ", timeit('s.insert(0,100)', 's = []', number=count)

count = 10000
print "collections", timeit('s.appendleft(100)', 'import collections; s = collections.deque()', number=count)
print "lists      ", timeit('s.insert(0,100)', 's = []', number=count)

1
