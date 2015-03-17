def printf(format, *args):
	print format % args,



s = "IV"
printf("%2s", s)
printf("%2s", s)
	
# using scalars
x = 100
y = 200
printf("x and y are %i and %i \n", x, y)


# using lists
primes = 2, 3, 5, 7, 11
printf("%3i %3i %3i %22i %3i \n", *primes) # must flatten tuple

1
