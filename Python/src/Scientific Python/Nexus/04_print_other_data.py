import h5py
file = h5py.File('i22-4996.nxs','r')


for d in file['entry1/Calibration/data']:
    print d, type(d)

for d in file['entry1/TfgTimes/data']:
    print d, type(d)
