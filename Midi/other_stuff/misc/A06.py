import sys
sys.path.append("library")

import library.myrtmidi as myrtmidi
from library.mymidi import Tracks

"""
+Tempo100
+TubularBells
+EFlatMajor
  0c # c
  1c # c+ d-
  2c # d
  3c # d+ e-
  4c # e
  5c # f
  6c # f+ g-
  7c # g
  8c # g+ A-
  9c # A
 10c # A+ B-
 11c # B (middle of clef)
 12c # C
 13c # C+ D-
 14c # D
 15c # D+ E-
 16c # E
 17c # F
 18c # F+ G-
 19c # G
 20c # G+ AA-
 21c # AA
 22c # AA+ BB-
 23c # BB
 24c # CC

E-         F         G         A-         B-         C         D         E-
3          5         7         8           10         12        14        15

   [16] 14 {5 +natural 9c} 14 {+flat 5 7c} [8] +rest {9 +flat 17c}
--      14, {5, 9},        14,    {5, 7},       0,   {9, 17}
--       2      2           2         2         4         4
 [16] +natural 11 {12 17c} 9 {11 17c} [8] +rest [16] +natural 14 {5 12c} +bar

[4] +natural 9 [16] 12 9 7 +natural 11 [4] +rest 12 +bar

[16] {5 +natural 9c} 14 {+flat 5 9c} 14 [8] 7 {9 12c} [8] +rest
 [16] 14 {+natural 5 9c}  14 [8] {+flat +dot 5 +dot 7c} +bar

[8] 5 {+natural 9 12c} 9 {12 +flat 17c} [2] +rest
+bar

+auto-beam

+bass
+TubularBells
+EFlatMajor
[4] 9 [8] 11 +natural 7 [4] 11 [8] 7 11 +bar
[2] 9 11 +bar
[8] +natural 7 11 [4] +rest [8] 11 7 [4] +rest +bar
[8] +natural 7 +flat 14 [4] +rest [2] +rest
"""

def tune(m):
    m += [14, {5, 9}, 14, {5, 7}, 0, {9, 17}],   \
         [2,      2,   2,      2, 4,       4]

m = myrtmidi.Midi(480)
tracks = Tracks("A06a", 2)
t1 = tracks.addTrack("Track 1")
t2 = tracks.addTrack("Track 2")
tracks.setTempo(480)
t1.setInstrument("Tubular Bells", channel = 1, pitchShift = 60)
t2.setInstrument("Tubular Bells", channel = 2, volume = 100, pitchShift = 48)
ch1 = m.createChannel("Tubular Bells", channel = 1, pitchShift = 60)
ch2 = m.createChannel("Tubular Bells", channel = 2, volume = 100, pitchShift = 48)

for ch in m.getChannels(): tune(ch)
for t in tracks.getTracks(): tune(t)

# m.dump()
m.play()
tracks.play()
