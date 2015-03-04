"""
Write a program that prints out the square, cubes and fourth 
power of the first 20 integers.
"""

format = "%6s"
print (format % "N"),(format % "N**2"),(format % "N**3"),(format % "N**4")

format = "%6i"
for i in range(1,21):
    print (format % i),(format % i**2),(format % i**3),(format % i**4)

1