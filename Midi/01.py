

def tune2(m):
    m += [72, 69, 64, 69, 72, 77, 72, 69], \
         [24, 24, 24, 24, 24, 24, 4, 4]
def tune(m):
    m += [72, 69, 64, 69, 72, 77, 72, 69], \
         [24, 24, 24, 24, 24, 24, 4, 4]
    m += [72, 0, 70, 67, 62, 67, 70, 75], \
         [12, 16, 24, 24, 24, 24, 24, 24]
    m += [70, 67, 70, 0, 68, 65, 60, 65], \
         [4, 4, 12, 16, 24, 24, 24, 24]
    m += [68, 73, 68, 65, 68, 0, 68, 65], \
         [24, 24, 4, 4, 12, 16, 4, 4]
    m += [68, 65, 68, 65, 68, 71, 74, 77], \
         [4, 4, 4, 4, 4, 4, 4, 4]
    m += [77, 74, 72, 69, 64, 0, 68, 65], \
         [4, 4, 24, 24, 24, 32, 4, 4]
    m += [68, 73, 70, 67, 70, 73, 76, 73], \
         [4, 24, 24, 24, 24, 24, 24, 4]
    m += [70, 73, 66, 63, 66, 71, 68, 65], \
         [4, 12, 4, 4, 4, 24, 24, 24]
    m += [68, 71, 74, 71, 68, 71, 64, 61], \
         [24, 24, 24, 4, 4, 12, 4, 4]
    m += [64, 69, 66, 63, 66, 69, 72, 69], \
         [4, 24, 24, 24, 24, 24, 24, 4]
    m += [66, 69, 0, 72, 69, 64, 69, 72], \
         [4, 12, 32, 24, 24, 24, 24, 24]
    m += [77, 72, 69, 72, 0, 70, 67, 62], \
         [24, 4, 4, 12, 16, 24, 24, 24]
    m += [67, 70, 75, 70, 67, 70, 0, 68], \
         [24, 24, 24, 4, 4, 12, 16, 24]
    m += [65, 60, 65, 68, 73, 68, 65, 68], \
         [24, 24, 24, 24, 24, 4, 4, 12]
    m += [0, 68, 65, 68, 65, 68, 65, 68], \
         [16, 4, 4, 4, 4, 4, 4, 4]
    m += [71, 74, 77, 77, 74, 72, 69, 64], \
         [4, 4, 4, 4, 4, 24, 24, 24]
    m += [69, 0], \
         [32, 32]

import sys
sys.path.append("library")
from library.mymidi import Tracks
tracks = Tracks("01", 3)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
t3 = tracks.addTrack("Track 3")
tracks.setTempo(70 * 32)
t1.setInstrument("Pad 8 (sweep)", channel = 1, pitchShift = 12)
t2.setInstrument("Pad 8 (sweep)", channel = 8, pitchShift = -12)
t3.setInstrument("Orchestral Harp", channel = 3)
for t in tracks.getTracks(): tune(t)
tracks.play()

'''
        "Pad 1 (new age)" : 89 ,
        "Pad 2 (warm)" : 90 ,
        "Pad 3 (polysynth)" : 91 ,
        "Pad 4 (choir)" : 92 ,
        "Pad 5 (bowed)" : 93 ,
        "Pad 6 (metallic)" : 94 ,
        "Pad 7 (halo)" : 95 ,
        "Pad 8 (sweep)" : 96 ,
'''
import library.myrtmidi as myrtmidi
m = myrtmidi.Midi(64 * 48, debug = False)
ch1 = m.createChannel("Pad 2 (warm)", channel = 1, volume = 127, pitchShift = 0)
ch2 = m.createChannel("Orchestral Harp", channel = 2, volume = 127, pitchShift = -12)
ch3 = m.createChannel("Acoustic Grand Piano", channel = 3, volume = 80)
# for ch in m.getChannels(): tune(ch)
# tune(ch1)
# tune(ch2)
# tune(ch3)
# m.play()

