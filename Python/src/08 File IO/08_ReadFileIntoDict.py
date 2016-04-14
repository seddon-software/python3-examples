

def getFileContents(filename):
    try: 
        f = open(filename, "r")
        allLines = f.readlines()
        return allLines
    except IOError,e:
        print e
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws


salary = {}
lines = getFileContents("data/salaries.txt")

for line in lines:
    key, value = line.split(',')
    key = key.strip()
    value = value.strip()
    salary[key] = value

# perform a lookup on (Zoe:23900)    
print "Zoe : ", salary["Zoe"]

# print dictionary in lexical order
sortedKeys = salary.keys()
sortedKeys.sort()

# print out salaries in lexical order
for key in sortedKeys:
    print key, ":", salary[key]

1

