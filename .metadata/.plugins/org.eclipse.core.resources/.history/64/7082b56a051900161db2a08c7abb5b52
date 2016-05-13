############################################################
#
#    Reading a file
#
############################################################

# successful read
try: 
    f = open("data/hello.txt", "r")
    try:
        for line in f:
            print line,
    finally:
        f.close()
except IOError,e:
    print e


# unsuccessful read
try: 
    f = open("./data/unknown-file.txt", "r")
    try:
        for line in f:
            print line,
    finally:
        f.close()
except IOError,e:
    print e

print "finished"