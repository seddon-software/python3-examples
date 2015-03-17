fm1 = "%6i"
fm2 = "%6i"
fm = fm1 + fm2

for x in range(10):
    print(fm % (x, x * x))
    print("%6i%6i" % (x, x * x))
