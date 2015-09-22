import sys
sys.path.append("library")

from library.mymidi import Tracks



def tune(m):
    m += [{62,80} ,{65,77} ,{68,74} ,71 ,62 ,65 ,68 ,65 ], \
         [16, 16, 16, 32, 8, 8, 8, 8]
    m += [62 ,80 ,77 ,74 ,77 ,80 ,0 ,75 ], \
         [8, 8, 8, 8, 8, 8, 16, 16]
    m += [72 ,72 ,71 ,{68,74} ,{65,77} ,{62,80} ,{65,77} ,{68,74} ], \
         [16, 16, 32, 16, 16, 16, 16, 16]
    m += [71 ,80 ,77 ,74 ,77 ,80 ,65 ,68 ], \
         [32, 8, 8, 8, 8, 8, 8, 8]
    m += [71 ,68 ,65 ,0 ], \
         [8, 8, 8, 16]
                  
tracks = Tracks("02", 2)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
tracks.setTempo(60 * 32)
t1.setInstrument("Acoustic Grand Piano", channel = 1)
t2.setInstrument("Pad 8 (sweep)", channel = 2)
for t in tracks.getTracks(): tune(t)

tracks.play()
