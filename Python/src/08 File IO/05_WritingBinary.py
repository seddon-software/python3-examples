############################################################
#
#    binary data
#
############################################################

# 3 different ways of working with binary data:
#    1. use str
#    2. use bytearray
#    3. use struct

def writeBinary(filename, data):
    try: 
        f = open(filename, "wb")
        f.write(data)
    except IOError,e:
        print e
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws


# use a str
data = "\x5F\x9D\x3E\x5F\x00\x00\x00\x00\x9D\x3E\x5F\x9D\x3E\x5F\x9D\x3E\x5F\x9D\x3E"
writeBinary('data/myfile-1.bin', data)


# use a bytearray
data = bytearray([0x5F,0x9D,0x3E,0x5F,0x00,0x00,0x00,0x00,0x9D,0x3E,0x5F,0x9D,0x3E,0x5F,0x9D,0x3E,0x5F,0x9D,0x3E])
writeBinary('data/myfile-2.bin', data)

# use struct
import struct
import binascii
import ctypes

dataFormat = '{0}s'.format(len(data))
print 'struct format: {0}'.format(dataFormat)
rawBuffer = struct.Struct(dataFormat)
stringBuffer = ctypes.create_string_buffer(rawBuffer.size)

print 'Before  :', binascii.hexlify(stringBuffer.raw)
data = "\x5F\x9D\x3E\x5F\x00\x00\x00\x00\x9D\x3E\x5F\x9D\x3E\x5F\x9D\x3E\x5F\x9D\x3E"
rawBuffer.pack_into(stringBuffer, 0, data)
print 'After  :', binascii.hexlify(stringBuffer.raw)

writeBinary('data/myfile-3.bin', stringBuffer)


1
