#!/usr/bin/env python

wordsfile = "dictionary"
dictionaryFile = open(wordsfile, 'r')

lines = dictionaryFile.readlines()

histodata = {}
wordcount = 0
for word in lines:
    length = len(word)
    if length in histodata:	# We could use a try/catch here if we want
        histodata[length] += 1
    else:
        histodata[length] = 1

# Close the file
dictionaryFile.close()

def getHash(count, character='*', tuningFactor = 5):
	count *= tuningFactor # Add in a tuning factor so it doesn't look squat
	return character * (int(count))


wordcount = len(lines)
print wordcount
for wordLength, number in histodata.items():
    percent = (float(number) / wordcount) * 100
    # :05 would also do fixed point
    print ("{:>4}:\t{}\t({:2f})\t->\t {}").format(wordLength, number, percent, getHash(percent, "*"))

