#!/usr/bin/env python

def printDict(dict):
    for (word,  count) in dict.items():
        print "{} seen {} time(s)".format(word,  count)
    
word = ""
dict = {}
while(word != "quit"):
    word = raw_input("Enter a word: ")
    word = word.lower()

    if (word == "status"):
        printDict(dict)
    else:
        # Do we have the word
        check = dict.get(word)
        if (check == None):
            dict[word] = 1
        else:
            dict[word] += 1
