import sys
sys.path.append("library")

from library.mymidi import Tracks



def tune(m):
    m += [70, 73, 76, 69, 69, 72, 75, 68, 0], \
         [ 3,  3,  3,  8,  3,  3,  3,  8, 4]
    m += [70, 73, 76, 69, 69, 72, 75, 68, 0], \
         [ 3,  3,  3,  8,  3,  3,  3,  8, 4]
    m += [71 ,68 ,65 ,71 ,68 ,65 ,68, {68, 71} ], \
         [ 2,  1,  2,  1,  2,  1,  4,       8]
    m += [71, 68, 65, 71, 68, 65, {68, 71}, 68 ], \
         [ 2,  1,  2,  1,  2,  1,       4,   8]
  
    m += [74,  0, 73, 70, 67, 73, 70, 67, 70, 73, 76, 0 ], \
         [ 3,  2,  3,  2,  3,  3,  2,  3,  2,  3,  3, 8]
    m += [75,  0, 72, 69, 75, 72, 69, 72, 75, 78, 0 ], \
         [ 3,  2,  3,  2,  3,  3,  2,  3,  2,  3, 8]
  
    m += [71, 68, 65, 71, 68, 65, {68, 71}, 68 ], \
         [ 2,  1,  2,  1,  2,  1,       4,   8]
    m += [73, 70, 73, 76, 79, 76, 73, 70, 73, 70, 67, 70, 0], \
         [ 1,  2,  3,  2,  1,  1,  2,  3,  2,  1,  2,  1, 8]
    m += [71 ,68 ,65 ,71 ,68 ,65 ,68, {68, 71} ], \
         [ 2,  1,  2,  1,  2,  1,  4,       8]
         
    m += [70, 73, 76, 69, 69, 72, 75, {68, 65}, 0], \
         [ 3,  3,  3,  8,  3,  3,  3,        8, 4]

tracks = Tracks("07", 3)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
t3 = tracks.addTrack("Track 3")
tracks.setTempo(64 * 6)
t1.setInstrument("Acoustic Grand Piano", channel = 1, volume = 127)
t2.setInstrument("Pad 8 (sweep)", channel = 2, pitchShift=-12, volume = 80)
t3.setInstrument("Synth Strings 2", channel = 3, pitchShift=-12, volume = 40)
for t in tracks.getTracks(): tune(t)

tracks.play()
