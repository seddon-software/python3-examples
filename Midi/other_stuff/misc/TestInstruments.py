import sys
sys.path.append("library")

import library.myrtmidi as myrtmidi
from library.mymidi import Tracks


def verse1(m):
    m += [{69, 74}, 65, {69, 74}, 65, 71],   \
         [       1,  1,        1,  1,  4]
    m += [{67, 71}, 71, {69, 74}, 67, 72],   \
         [       1,  1,        1,  1,  4]
    m += [69, {65, 74}, 72, 71, 65, {65, 71}],   \
         [ 1,        1,  1,  1,  1,       3]
    m += [74, 77, 72, 69, 67, 72],   \
         [ 1,  1,  1,  1,  1,  3]

def verse2(m):
    m += [67, 71, 73, 71, 69, 72],   \
         [ 1,  1,  1,  1,  1,  3]
    m += [{67, 71}, 71, {69, 74}, 71, {65, 69}],   \
         [      1,   1,       1,   1,       4]
    m += [67, 74, 76, 74, 69, 72],   \
         [ 1,  1,  1,  1,  1,  3]
    m += [{67, 71}, 71, {69, 74}, 69, {71, 74}],   \
         [      1,   1,        1,  1,       4]

def verse3(m):
    m += [{69, 74}, 65, {69, 74}, 65, 71],   \
         [       1,   1,       1,  1,  4]
    m += [{67, 71}, 71, {69, 74}, 67, 72],   \
         [       1,   1,       1,  1,  4]
    m += [69, {65, 74}, 72, 71, 65, {65, 71}],   \
         [ 1,        1,  1,  1,  1,        3]
    m += [74, 77, 72, 69, 67, 72],   \
         [ 1,  1,  1,  1,  1,  3]

def verse4(m):
    m += [{69, 74}, {67, 71}, 69, {71,74}, {71, 74}, 74, {69, 74}],   \
         [       1,        2,  1,       2,        1,  1,        4]
    m += [{69, 74}, 76, {71,74}, 78, 76, 74, 76],   \
         [       1,  4,       1,  2,  1,  1,  4]
    m += [{69, 74}, {67, 71}, 69, {71,74}, {71, 74}, 74, {69, 74}],   \
         [       1,        2,  1,       2,        1,  1,        4]
    m += [{69, 74}, 76, {71,74}, 78, 74, 69, 72],   \
         [       1,  4,       1,  2,  1,  1,  4]

def verse5(m):
    m += [69, 71, 69, 74, 74, 76, 74,  {65, 71}],   \
         [ 1,  1,  1,  1,  1,  1,  1,        5]
    m += [71, 69, 74, 74, 76, 74,  {71, 77}, 0],   \
         [ 1,  1,  1,  1,  1,  1,        4,  1]
    m += [71, 69, 74, 69, 74, 65, 71],   \
         [ 1,  1,  2,  1,  1,  1,  3]
    m += [67, 71, {71, 74}, 72, 71, 74, 72],   \
         [ 1,  1,        1,  1,  1,  1,  4]

def tune(m):
    m += [0], [4]
    verse1(m)
    verse1(m)
    m += [0], [2]
    verse2(m)
    verse3(m)
    m += [0], [2]
    verse4(m)
    verse5(m)
    verse1(m)
    m += [0], [4]

m = myrtmidi.Midi(240)
# ch1 = m.createChannel("Acoustic Grand Piano", channel = 1 )
# ch2 = m.createChannel("Pad 6 (metallic)",     channel = 2, volume = 100)
# ch3 = m.createChannel("Acoustic Bass",        channel = 3, volume = 100, pitchShift = -24)
ch4 = m.createChannel("Acoustic Grand Piano", channel = 4, pitchShift = -12)
# ch5 = m.createChannel("Bassoon",              channel = 5, volume = 80, pitchShift = -12)

for ch in m.getChannels(): tune(ch)
m.play()
