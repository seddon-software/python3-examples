#!/usr/bin/env python

import sys

wordsfile = "dictionary"
dictionaryFile = open(wordsfile, 'r')

lines = dictionaryFile.readlines()

histodata = {}
wordcount = 0
for word in lines:
    length = len(word)
    try:
        histodata[length] += 1
    except KeyError as ex:
        histodata[length] = 1
        
def getHash(count, character='*', tuningFactor = 5):
	count *= tuningFactor # Add in a tuning factor so it doesn't look squat
	return character * (int(count))


wordcount = len(lines)
print wordcount
for wordLength, number in histodata.items():
    percent = (float(number) / wordcount) * 100
    print "%d:\t%d\t(%f)\t->\t %s" % (wordLength, number, percent, getHash(percent, 'X'))

