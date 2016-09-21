import sys
from lore.tree import notes
sys.path.append("library")

from library.mymidi import Tracks
import library.myrtmidi as myrtmidi



def rest(m, n):
    m += [0],[n] 

def ch1(n): return n
def ch2(n): return { n, n+3 }
def ch3(n): return { n, n+3, n+6 }
    
def w4(m, fn, duration, *notes):
    notes = list(notes)
    last = notes.pop()
    for n in notes:
        m += ([0],[duration]) if n == 0 else ([fn(n)], [duration])  
    m += ([0],[duration*2]) if last == 0 else ([fn(last)], [duration*2])  

def w3(m, fn, *notes):
    for n in notes:
        m += ([0],[4]) if n == 0 else ([fn(n)], [4])  

def tune(m):
    rest(m, 4)
#     w4(m, ch3, 4, 0,61, 0,62, 0,63, 0,64)
#     w4(m, ch2, 4, 0,63,62,61,61,62,64,62,61)
#     w4(m, ch3, 4, 0,63, 0,64, 0,65, 0,66)
#     w4(m, ch2, 4, 0,65,64,63,63,64,66,63)
#     w4(m, ch2, 4, 0,64,63,62,61,61,62,64,62,61)
#     rest(m, 4)
#     w4(m, ch3, 4, 0,63, 0,64, 0,65, 0,66)
#     w4(m, ch2, 4,65,64,63,63,64,66,63)
#     w4(m, ch3, 4, 0,64, 0,63, 0,62, 0,61)
#     w4(m, ch2, 4,61,62,64,62,61,62,61,63)
#     w4(m, ch3, 4, 0,66, 0,65, 0,64, 0,63)
#     w4(m, ch2, 4,63,64,65,64,63,62,64,63)
    w4(m, ch2, 3, 0,61,62,64,62,64,62,61,62,61,62,64,62)
    w4(m, ch3, 4, 0,58, 0,60, 0,62, 0,64)
    w4(m, ch3, 4, 0,62, 0,64, 0,66, 0,68)
    w4(m, ch3, 2, 0,64, 0,64, 0, 0,63, 0,63)
    w4(m, ch3, 2, 0, 0,62, 0,62, 0, 0)
    w4(m, ch3, 4, 61)
    rest(m, 4)
    

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


