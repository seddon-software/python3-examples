import sys
from lore.tree import notes
sys.path.append("library")

from library.mymidi import Tracks
import library.myrtmidi as myrtmidi

def rest(m,d):
    m += [0],[d]
    
def f(m,n,d):
    n += 60
    m += [{n,n+3,n+6},0], [d,d]

def g(m,n,d):
    n += 60
    m += [{n,n+3}], [d,d] 

def tune(m):
    rest(m, 4)
    f(m,1,4)
    f(m,2,4)
    f(m,3,4)
    f(m,4,4)
    g(m,3,4)
    g(m,2,4)
    g(m,1,4)
    g(m,1,4)
    g(m,2,4)
    g(m,4,4)
    g(m,2,4)
    g(m,1,8)
    rest(m,8)

    f(m,3,4)
    f(m,4,4)
    f(m,5,4)
    f(m,6,6)
    rest(m,4)


# [16] {5 8c}
# [16] {4 7c}
# [16] {3 6c}
# [16] {3 6c}
# [16] {4 7c}
# [16] {6 9c}
# [8] {3 6c} +rest
# 
# # 3 #######################################
# 
# [8]  {4 7c}
# [16] {3 6c}
# [16] {2 5c}
# [16] {1 4c}
# [16] {1 4c}
# [16] {2 5c}
# [16] {4 7c}
# [16] {2 5c}
# [8]  {1 4c} +rest
# 
# # 4 #######################################
# 
# [16] {3 6c 9c} +rest
# [16] {4 7c 10c} +rest
# [16] {5 8c 11c} +rest
# [16] +dot {6 9c 12c}
# 
# [16] {5 8c}
# [16] {4 7c}
# [16] {3 6c}
# [16] {3 6c}
# [16] {4 7c}
# [16] {6 9c}
# [8] {3 6c} [4] +rest
# 
# # 5 #######################################
# 
# [16] {4 7c 10c} +rest
# [16] {3 6c 9c} +rest
# [16] {2 5c 8c} +rest
# [16] {1 4c 7c} +rest
# [16] {1 4c}
# [16] {2 5c}
# [16] {4 7c}
# [16] {2 5c}
# [16] {1 4c}
# [16] {2 5c}
# [16] {1 4c}
# [8]  {3 6c} [4] +rest
# 
# # 6 #######################################
# 
# [16] {6 9c 12c} +rest
# [16] {5 8c 11c} +rest
# [16] {4 7c 10c} +rest
# [16] {3 6c 9c} +rest
# [16] {3 6c}
# [16] {4 7c}
# [16] {5 8c}
# [16] {4 7c}
# [16] {3 6c}
# [16] {2 5c}
# [16] {4 7c}
# [8]  {3 6c} +rest
# 
# # 7 #######################################
# 
# [16] {1 4c}
# [16] {2 5c}
# [16] {4 7c}
# [16] {2 5c}
# 
# [16] {4 7c}
# [16] {2 5c}
# [16] {1 4c}
# [16] {2 5c}
# 
# [16] {1 4c}
# [16] {2 5c}
# [16] {4 7c}
# [16] {2 5c}
# 
# 
# 
# [16] {-2 1c 4c} +rest
# [16]  {0 3c 6c} +rest
# [16]  {2 5c 8c} +rest
# [16]  {4 7c 10c} +rest
# 
# [16]  {2 5c 8c} +rest
# [16]  {4 7c 10c} +rest
# [16]  {6 9c 12c} +rest
# [16]  {8 11c 14c} +rest
# 
# [32] {4 7c 10c} +rest
# [16] +dot {4 7c 10c} +rest
# [32] {3 6c 9c} +rest
# [16] +dot {3 6c 9c} +rest
# [32] {2 5c 8c} +rest
# [16] +dot {2 5c 8c} +rest
# [8]  {1 4c 7c} +rest
    rest(m, 8)

    

tracks = Tracks("11", 4)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
t3 = tracks.addTrack("Track 3")
t4 = tracks.addTrack("Track 4")
tracks.setTempo(64 * 16)
t1.setInstrument("Acoustic Grand Piano", channel = 1)
t2.setInstrument("Pad 8 (sweep)", channel = 2, pitchShift = -12)
t3.setInstrument("Pad 8 (sweep)", channel = 3, pitchShift = -24)
t4.setInstrument("Pad 8 (sweep)", channel = 4, pitchShift = 0)
for t in tracks.getTracks(): tune(t)
tracks.play()

m = myrtmidi.Midi(480)
c1 = m.createChannel("Acoustic Grand Piano", channel = 1)
c2 = m.createChannel("Pad 8 (sweep)", channel = 2, pitchShift = -12)
c3 = m.createChannel("Pad 8 (sweep)", channel = 3, pitchShift = -24)
c4 = m.createChannel("Pad 8 (sweep)", channel = 4, pitchShift = 0)
for c in m.getChannels(): tune(c)
# m.play()


