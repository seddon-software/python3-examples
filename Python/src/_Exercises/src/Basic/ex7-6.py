"""
Write a program that reads a file, reverses the order of lines in 
the file and then saves the changes in a new file.
"""

inFile = None
outFile = None

try:
    inFile = open("../data/original.txt", "r")
    outFile = open("../data/reversed.txt", "w")

    listOfLines = list()
    for line in inFile:
        listOfLines.insert(0, line)
    
    for line in listOfLines:
        outFile.write(line)
        
except IOError, reason:
    print reason
finally:        
    if inFile: inFile.close()
    if outFile: outFile.close()


1