import sys
sys.path.append("library")

import library.myrtmidi as myrtmidi
from library.mymidi import Tracks

def verse1(m):
    m += [12, 14, 14, 9, 12],   \
         [12,  4,  8, 4,  4]
    m += [ 9, 14,  0, 14],   \
         [ 4, 12,  8, 12]
    m += [14, 16, 16, 16, 11, 14, 11],   \
         [ 4,  4,  8,  4,  4,  4,  4]
    m += [16,  0, 16, 16, 17],   \
         [16,  2,  4,  8,  4]
    m += [17, 16, 16, 7, 9, 11],   \
         [ 8,  4,  4, 4, 4,  4]
    m += [ 0,  7, 12, 7, 9, 12],   \
         [ 4, 12,  4, 4, 4,  4]
    m += [14, 12, 14, 9, 12, 7,  5],   \
         [ 8,  8,  4, 4,  4, 4, 32]

def tune(m):
    m += [0], [4]
    verse1(m)
    m += [0], [4]

m = myrtmidi.Midi(64*16)
tracks = Tracks("A04", 4)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
t3 = tracks.addTrack("Track 3")
t4 = tracks.addTrack("Track 4")
tracks.setTempo(240 * 4)
t1.setInstrument("Acoustic Grand Piano", channel = 1, pitchShift = 60)
t2.setInstrument("Acoustic Grand Piano", channel = 2, volume = 100, pitchShift = 48)
t3.setInstrument("Melodic Tom", channel = 3, volume = 80, pitchShift = 36)
t4.setInstrument("Tremolo Strings", channel = 4, volume = 100, pitchShift = 36)
ch1 = m.createChannel("Acoustic Grand Piano", channel = 1, pitchShift = 60)
ch2 = m.createChannel("Acoustic Grand Piano", channel = 2, volume = 100, pitchShift = 48)
ch3 = m.createChannel("Melodic Tom", channel = 3, volume = 80, pitchShift = 36)
ch4 = m.createChannel("Tremolo Strings", channel = 4, volume = 100, pitchShift = 36)

for ch in m.getChannels(): tune(ch)
for t in tracks.getTracks(): tune(t)

# m.dump()
m.play()
# tracks.play(debug = True)

