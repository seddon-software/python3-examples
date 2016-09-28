import sys
sys.path.append("library")

from library.mymidi import Tracks

def tune1(m):
    m += [68 ,69 ,68 ,68 ,67 ,66 ,65 ,64 ], \
         [1, 1, 2, 2, 2, 2, 2, 2]
    m += [0 ,68 ,69 ,68 ,68 ,67 ,66 ,64 ], \
         [2, 1, 1, 2, 2, 2, 2, 4]
    m += [68 ,69 ,68 ,68 ,67 ,66 ,65 ,64 ], \
         [1, 1, 2, 2, 2, 2, 2, 2]
    m += [0 ,68 ,69 ,68 ,68 ,67 ,66 ,64 ], \
         [2, 1, 1, 2, 2, 2, 2, 4]
         
def tune2(m):
    m += [60 ,59 ,60 ,59 ,60 ,59 ,60 ,59 ], \
         [1, 1, 2, 2, 1, 1, 2, 2]
    m += [60 ,59 ,60 ,59 ,60 ,59 ,60 ,59 ], \
         [1, 1, 2, 2, 1, 1, 2, 2]
    m += [60 ,59 ,60 ,59 ,60 ,59 ,60 ,59 ], \
         [1, 1, 2, 2, 1, 1, 2, 2]
    m += [60 ,59 ,60 ,59 ,60 ,59 ,60 ,59 ], \
         [1, 1, 2, 2, 1, 1, 2, 2]
    m += [60 ,59 ,60 ,59 ,60 ,59 ,60 ,59 ], \
         [1, 1, 2, 2, 1, 1, 2, 2]

tracks = Tracks("05", 2)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
tracks.setTempo(64 * 8)
t1.setInstrument("Acoustic Grand Piano", channel = 1)
t2.setInstrument("Synth Drum", channel = 2)
tune1(t1)
tune2(t2)
tracks.play()
