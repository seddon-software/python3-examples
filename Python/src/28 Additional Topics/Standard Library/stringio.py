############################################################
#
#    string IO
#
############################################################

# Use stringIO to simulate a stream of character of binary data

from StringIO import StringIO

str=StringIO()
str.write("This is a stream ")
str.write("of character data ")
str.write("that can be written ")
str.write("to a stream device")
print str.getvalue()

bin=StringIO()
bin.write("\x41\x42\x43\x44\x45\x46")
file = open ("../data/test.bin","wb")
file.write(bin.getvalue())
file.close()


1