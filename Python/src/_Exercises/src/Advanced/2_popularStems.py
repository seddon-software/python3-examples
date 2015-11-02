"""
Words prefixes are also called stems. Write a program that reads 
a file with one word per input line and finds the most 
popular stems of size 2 to 6.
"""


def DetermineStems():
    '''
       build a dictionary of (stem, count) pairs
    '''
    for word in lines:
        word = word.rstrip()
        for i in range(2, len(word)+1):
            stem = word[:i]
            if stem in stems:
                stems[stem] += 1
            else:
                stems[stem] = 1

def openTestData():
    '''
       build an list containing the test data
    '''
    inFile = None
    lines = list()
    
    try:
        inFile = open("../data/stems.txt", "r")
    
        for line in inFile:
            lines.append(line)
    except IOError, reason:
        print reason
    finally:        
        if inFile: inFile.close()
    
    return lines

def ProcessStems():
    '''
       build a list containing (stem, count) tuples
       - element 2 contains the most popular 2 stem 
       - element 3 contains the most popular 3 stem 
       - element 4 contains the most popular 4 stem ...
    ''' 
    for i in range(20): #assume word never exceed 19 characters
        popularStems.append((None, None))
        
    for key, value in stems.iteritems():
        #print key, value
        index = len(key)
        if popularStems[index][1] < value:
            popularStems[index] = (key, value)
    return popularStems
    
def PrintResults():
    '''
       popularStems contains a set of tuples
    '''
    for i in range(2,7):
        stem = popularStems[i][0] 
        count = popularStems[i][1]
        if stem != None:
            print "Most popular stem of size " + str(i) + " " + \
                  stem + " (occurs " + str(count) + " times)" 
     
stems = dict()
popularStems = list()
lines = openTestData()
DetermineStems()
ProcessStems()
PrintResults()

1