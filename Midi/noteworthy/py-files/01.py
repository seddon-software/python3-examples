
import sys
sys.path.append("../..")
from library.mymidi import Tracks
tracks = Tracks("01", 5)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
t3 = tracks.addTrack("Track 3")
t4 = tracks.addTrack("Track 4")
t5 = tracks.addTrack("Track 4")
t1.setInstrument("Pad 8 (sweep)", channel = 1, pitchShift = -12, volume = 100)
t2.setInstrument("Orchestral Harp", channel = 2, pitchShift = 0, volume = 60)
t3.setInstrument("Synth Drum", channel = 3, pitchShift = -12, volume = 20)
t4.setInstrument("Bright Acoustic Piano", channel = 4, pitchShift = 0, volume = 0)
t5.setInstrument("Pad 8 (sweep)", channel = 5, pitchShift = 12, volume = 100)

def tune(m):
    m += [72, 69, 64, 69, 72, 77, 72, 69], \
         [36, 36, 36, 36, 36, 36, 6, 6]
    m += [72, 0, 70, 67, 62, 67, 70, 75], \
         [18, 24, 36, 36, 36, 36, 36, 36]
    m += [70, 67, 70, 0, 68, 65, 60, 65], \
         [6, 6, 18, 24, 36, 36, 36, 36]
    m += [68, 73, 68, 65, 68, 0, 68, 65], \
         [36, 36, 6, 6, 18, 24, 6, 6]
    m += [68, 65, 68, 65, 68, 71, 74, 77], \
         [6, 6, 6, 6, 6, 6, 6, 6]
    m += [77, 74, 72, 69, 64, 0, 68, 65], \
         [6, 6, 36, 36, 36, 48, 6, 6]
    m += [68, 73, 70, 67, 70, 73, 76, 73], \
         [6, 36, 36, 36, 36, 36, 36, 6]
    m += [70, 73, 66, 63, 66, 71, 68, 65], \
         [6, 18, 6, 6, 6, 36, 36, 36]
    m += [68, 71, 74, 71, 68, 71, 64, 61], \
         [36, 36, 36, 6, 6, 18, 6, 6]
    m += [64, 69, 66, 63, 66, 69, 72, 69], \
         [6, 36, 36, 36, 36, 36, 36, 6]
    m += [66, 69, 0, 72, 69, 64, 69, 72], \
         [6, 18, 48, 36, 36, 36, 36, 36]
    m += [77, 72, 69, 72, 0, 70, 67, 62], \
         [36, 6, 6, 18, 24, 36, 36, 36]
    m += [67, 70, 75, 70, 67, 70, 0, 68], \
         [36, 36, 36, 6, 6, 18, 24, 36]
    m += [65, 60, 65, 68, 73, 68, 65, 68], \
         [36, 36, 36, 36, 36, 6, 6, 18]
    m += [0, 68, 65, 68, 65, 68, 65, 68], \
         [24, 6, 6, 6, 6, 6, 6, 6]
    m += [71, 74, 77, 77, 74, 72, 69, 64], \
         [6, 6, 6, 6, 6, 36, 36, 36]
    m += [69], \
         [48]
tracks.setTempo(6720/2)

for t in tracks.getTracks():
    tune(t)
tracks.play()
