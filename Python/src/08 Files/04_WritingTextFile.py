############################################################
#
#    Writing to a file
#
############################################################

def writeFileContents(filename, data):
    try: 
        f = open(filename, "w+")
        f.writelines(data)
    except IOError,e:
        print e
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws

data = ("line 1\n", "line 2\n", "line 3\n", "line 4\n")
writeFileContents("data/text.txt", data)


1