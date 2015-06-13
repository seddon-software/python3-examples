#!/usr/bin/env python

def calculateVolumeOrArea(height,  width,  depth=None):
    area = float(height) * float(width)
    if (depth == None):
        volume = None
    else:
        volume = area * float(depth)
    
    return {'area': area,  'volume': volume}
    

height = raw_input("Height: ")
width = raw_input("Width: ")
depth = raw_input("Depth: ")

results = calculateVolumeOrArea(height, width)
print "\nArea: {}\nVolume: {}".format(results['area'],  results['volume'])

results = calculateVolumeOrArea(height,  width,  depth)
print "\nArea: {}\nVolume: {}".format(results['area'],  results['volume'])
