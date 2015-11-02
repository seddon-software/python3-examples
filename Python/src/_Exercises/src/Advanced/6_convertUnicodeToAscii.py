import os, codecs

# these functions use join to operate on a generator (the round brackets) for effeciency
def removeNonAscii(s): return "".join(i for i in s if ord(i)<=128)  # converts unicode to ascii
def convertHyphens(s): return u"".join(u'-' if ord(i)==0x2013 else i for i in s) # entirely unicode

def getUnicodeFileContents(filename):
    try: 
        with codecs.open(filename, mode="r", encoding="utf-8") as f:
            allLines = f.readlines()
            text = "".join(allLines)
            return text
    except IOError,e:
        print e

def writeAsciiFile(filename, data):
    try: 
        with open(filename, "w+") as f:
            f.writelines(data)
    except IOError,e:
        print e


os.chdir("resources")
unicodeText = getUnicodeFileContents("results_2014_15.unicode")
unicodeText = convertHyphens(unicodeText)
asciiText = removeNonAscii(unicodeText)
writeAsciiFile("results_2014_15.ascii", asciiText)
