############################################################
#
#    binary data
#
############################################################

# use 'array' for formatting large amounts binary data
# use 'struct' for smaller (fixed size) amounts
import array
import os

def readBinary(filename):
    try:
        size = os.stat(filename).st_size
        f = open(filename, "rb")
        chars = array.array('c')    # sets up a byte buffer
        chars.fromfile(f, size)     # populates the buffer
        return chars.tolist()       # return list of chars
    except EOFError,e:  # file doesn't contain chars
        print e
    except IOError,e:   # some other error
        print e
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws


charList = readBinary('data/myfile-1.bin')

print "%-10s%-10s" % ( "Decimal", "Hex" )
for ch in charList:
    # ord converts char to decimal
    # hex converts decimal to hex
    print "%-10s%-10s" % ( ord(ch), hex(ord(ch)) )


1