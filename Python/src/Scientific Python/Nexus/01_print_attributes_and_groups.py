import h5py
file = h5py.File('i22-4996.nxs','r')

def printListOfAttributes():
    print "attributes"
    print "=========="
    for attribute in file:
        print attribute
    print
    
def printListOfGroups():
    print "groups"
    print "======"    
    for group in file['entry1']:
        print group
    print

printListOfAttributes()
printListOfGroups()

import sys
sys.exit()
for x in file['entry1/Hotwaxs/data']:
    print x, len(x), type(x)
for x in file['entry1/Rapid2D/data']:
    print x, len(x), type(x)

for x in file['entry1/Hotwaxs']:
    print x, len(x), type(x)

print file['entry1/instrument/Hotwaxs/data'].shape
print file['entry1/Hotwaxs/data'].shape
print file['entry1/Rapid2D/data'].shape
print file['entry1/instrument/Rapid2D/data'].shape

for x in file['entry1/Calibration/data']:
    print x, len(x), type(x)

for x in file['entry1/TfgTimes/data']:
    print x, len(x), type(x)