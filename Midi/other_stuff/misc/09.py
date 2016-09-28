import sys
sys.path.append("library")

from library.mymidi import Tracks



def tune(m):
    m += [64 , 65 , 64 , 65 , 64 , 64 , 65 , 65 ], \
         [1, 1, 1, 1, 1, 1, 1, 1]
    m += [66 , 68 , 69 , 69 , 68 , 66 , 65 , 65 ], \
         [1, 1, 1, 1, 1, 1, 1, 1]
    m += [0 , 64 , 65 , 64 , 65 , 64 , 65 , 66 ], \
         [1, 1, 1, 1, 1, 1, 1, 1]
    m += [66 , 66 , 68 , 69 , 69 , 68 , 66 , 68 ], \
         [1, 1, 1, 1, 1, 1, 1, 1]
    m += [68 , 0 , 70 , 72 , 70 , 70 , 72 , 70 ], \
         [1, 1, 2, 1, 1, 1, 1, 2]
    m += [0 , 64 , 65 , 64 , 65 , 64 , 64 , 65 ], \
         [2, 1, 1, 1, 1, 1, 1, 1]
    m += [65 , 66 , 68 , 69 , 69 , 68 , 66 , 65 ], \
         [1, 1, 1, 1, 1, 1, 1, 1]
    m += [65 , 0 , 64 , 65 , 64 , 65 , 64 , 65 ], \
         [1, 1, 1, 1, 1, 1, 1, 1]
    m += [66 , 66 , 66 , 68 , 69 , 69 , 68 , 66 ], \
         [1, 1, 1, 1, 1, 1, 1, 1]
    m += [68 , 68 , 0 , 70 , 72 , 70 , 71 , 72 ], \
         [1, 1, 1, 2, 1, 1, 1, 1]
    m += [73 , 70 , 71 , 72 , 73 , 73 , 72 , 71 ], \
         [2, 1, 1, 1, 2, 2, 1, 1]
    m += [70 , 71 , 70 , 71 , 72 , 72 , 68 , 0 ], \
         [1, 1, 1, 1, 1, 1, 4, 4]


tracks = Tracks("09", 3)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
t3 = tracks.addTrack("Track 3")
tracks.setTempo(64 * 6)
t1.setInstrument("Electric Grand Piano", channel = 1, pitchShift=-6)
t2.setInstrument("Electric Grand Piano", channel = 2, pitchShift=-18, volume = 100)
t3.setInstrument("Synth Drum", channel = 3, pitchShift=-18, volume=100)

for t in tracks.getTracks(): tune(t)
tracks.play()
