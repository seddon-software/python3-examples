def readFile(filename):
    try:
        f = open(filename,"r")
        all = f.readlines()
        data = "".join(all) # convert to string
        f.close()
        return data
    except Exception, e:
        print "Invalid File"
        return []


1
    


