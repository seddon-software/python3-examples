"""
Write a program that counts the number of lines in a file.
"""

inFile = None
count = 0

try:
    inFile = open("../data/original.txt", "r")

    for line in inFile:
        count += 1
except IOError, reason:
    print reason
finally:        
    if inFile: inFile.close()

print "Line count = ", count


1