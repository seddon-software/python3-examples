import sys
sys.path.append("library")

from library.mymidi import Tracks



def tune(m):
    pass

tracks = Tracks("00", 1)
t1 = tracks.addTrack("Track 1")
tracks.setTempo(64 * 32)
t1.setInstrument("Acoustic Grand Piano", channel = 1)
for t in tracks.getTracks(): tune(t)

tracks.play()
