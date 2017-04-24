import tables as tb
import numpy as np

class Particle(tb.IsDescription):
    name      = tb.StringCol(16)   # 16-character String
    idnumber  = tb.Int64Col()      # Signed 64-bit integer
    ADCcount  = tb.UInt16Col()     # Unsigned short integer
    TDCcount  = tb.UInt8Col()      # unsigned byte
    grid_i    = tb.Int32Col()      # 32-bit integer
    grid_j    = tb.Int32Col()      # 32-bit integer
    pressure  = tb.Float32Col()    # float  (single-precision)
    energy    = tb.Float64Col()    # double (double-precision)

h5file = tb.open_file("tutorial1.h5", mode = "w", title = "Test file")
group = h5file.create_group("/", 'detector', 'Detector information')
table = h5file.create_table(group, 'readout', Particle, "Readout example")
particle = table.row

for i in range(10):
    particle['name']  = 'Particle: %6d' % (i)
    particle['TDCcount'] = i % 256
    particle['ADCcount'] = (i * 256) % (1 << 16)
    particle['grid_i'] = i
    particle['grid_j'] = 10 - i
    particle['pressure'] = float(i*i)
    particle['energy'] = float(particle['pressure'] ** 4)
    particle['idnumber'] = i * (2 ** 34)
    # Insert a new particle record
    particle.append()

table.flush()

table = h5file.root.detector.readout
pressure = [x['pressure'] for x in table.iterrows() if x['TDCcount'] > 3 and 20 <= x['pressure'] < 50]
print(pressure)

names = [ x['name'] for x in table.where("""(TDCcount > 3) & (20 <= pressure) & (pressure < 50)""") ]
print(names)

gcolumns = h5file.create_group(h5file.root, "columns", "Pressure and Name")
h5file.create_array(gcolumns, 'pressure', np.array(pressure), "Pressure column selection")
h5file.create_array(gcolumns, 'name', names, "Name column selection")
h5file.close()

def useUtilities():
    import os, sys
    bin = os.path.dirname(sys.executable) + os.pathsep
    os.environ["PATH"] = bin + os.environ["PATH"]
    os.system("ptdump tutorial1.h5")
    os.system("h5ls -rd tutorial1.h5")

useUtilities()
