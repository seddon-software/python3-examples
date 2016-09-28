import sys
sys.path.append("library")

from library.mymidi import Tracks



def tune(m):
    m += [72 ,75 ,72 ,70 ,68 ,72 ,70 ,69 ], \
         [2, 4, 2, 4, 2, 4, 2, 3]
    m += [67 ,65 ,0 ,70 ,73 ,70 ,68 ,66 ], \
         [3, 4, 4, 2, 4, 2, 4, 2]
    m += [68 ,66 ,65 ,63 ,61 ,0 ,66 ,68 ], \
         [4, 2, 3, 3, 4, 4, 2, 4]
    m += [70 ,68 ,70 ,68 ,66 ,71 ,73 ,71 ], \
         [2, 4, 2, 4, 2, 3, 3, 4]
    m += [0 ,70 ,68 ,66 ,68 ,70 ,68 ,70 ], \
         [4, 2, 4, 2, 4, 2, 4, 2]
    m += [65 ,63 ,61 ,0 ], \
         [3, 3, 4, 8]
tracks = Tracks("04", 3)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
t3 = tracks.addTrack("Track 3")
tracks.setTempo(64 * 8)
t1.setInstrument("Orchestral Harp", channel = 1, pitchShift=-12)
t2.setInstrument("Pad 8 (sweep)", channel = 2)
t3.setInstrument("Soprano Sax", channel = 3, pitchShift=-12)
for t in tracks.getTracks(): tune(t)

tracks.play()
