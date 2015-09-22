import sys
sys.path.append("library")

import library.myrtmidi as myrtmidi
from library.mymidi import Tracks

def main():
    tracks = Tracks("17new", 2)
    t1 = tracks.addTrack("Track 1")
    t2 = tracks.addTrack("Track 2")
    tracks.setTempo(240)
    t1.setInstrument("Pad 6 (metallic)", channel = 2)
    t2.setInstrument("Acoustic Grand Piano", channel = 3)
# 93  : "Pad 5 (bowed)",
# 94  : "Pad 6 (metallic)",
# 95  : "Pad 7 (halo)",

    for t in tracks.getTracks(): tune(t)
    
    tracks.play()


def tune(m):
    m += [{65,70},{68,73},{62,65,70},{61,63,68},{63,65,70},{68,73},{65,70},{65,70}], \
        [2, 2, 1, 1, 2, 2, 2, 1]
    m += [{70,75},{68,73},{66,70,75},{71,76},{70,75},{71,76},{66,70,75},{68,73}], \
        [1, 2, 1, 1, 1, 4, 1, 1]
    m += [{70,75},{66,70},{66,70},{68,73},{63,66,70},{61,63,68},{63,66,70},{68,73}], \
        [2, 4, 2, 2, 1, 1, 4, 2]
    m += [{66,70},{66,70},{70,75},{68,73},{66,70,75},{71,76},{70,75},{71,76}], \
        [2, 1, 1, 2, 1, 1, 1, 2]
    m += [{66,70,75},{71,76},{70,75},{71,76},{64,68,73},{66,70,75}], \
        [1, 1, 2, 1, 1, 8]
    m += [{65,70},{68,73},{62,65,70},{61,63,68},{63,65,70},{68,73},{65,70},{65,70}], \
        [2, 2, 1, 1, 2, 2, 2, 1]
    m += [{70,75},{68,73},{66,70,75},{71,76},{70,75},{71,76},{66,70,75},{68,73}], \
        [1, 2, 1, 1, 1, 4, 1, 1]
    m += [{70,75},{66,70},{66,70},{68,73},{63,66,70},{61,63,68},{63,66,70},{68,73}], \
        [2, 4, 2, 2, 1, 1, 4, 2]
    m += [{66,70},{66,70},{70,75},{68,73},{66,70,75},{71,76},{70,75},{71,76}], \
        [2, 1, 1, 2, 1, 1, 1, 2]
    m += [{66,70,75},{71,76},{70,75},{71,76},{64,68,73},{66,70,75}], \
        [1, 1, 2, 1, 1, 8]

main()
