fileName = "z4.mid"
f = open(fileName, "wb")

from MidiEvent import MidiEvent
        

def writeHeaderChunk():
    m = MidiEvent()    
    m.addHeaderChunk(tracks = 2, tempo = 128 * 4)
    buffer = m.getBuffer()
    f.write(buffer)
writeHeaderChunk()
                      
def writeTrackChunk():
    m = MidiEvent()
    m.addTrackHeader()
    m.setTrackName("Track 1")
    m.setCopyright("(C) CRS Enterprises Ltd")
    m.setInstrument(channel = 0, voice = 0)
    for n in range(12):
        note = 60 + n
        duration = 500 + 500 * (n % 2)
        m.noteOnOff(note, duration)

    m.endTrack()
    buffer = m.getBuffer()
    f.write(buffer)
writeTrackChunk()

def writeTrackChunk2():
    m = MidiEvent()
    m.addTrackHeader()
    m.setTrackName("Track 2")
    m.setCopyright("(C) CRS Enterprises Ltd")
    m.setInstrument(channel = 1, voice = 10)
    m.setTime(10000)
    for n in range(12):
        note = 60 + n
        m.noteOnOff(note, 1000)

    m.endTrack()
    buffer = m.getBuffer()
    f.write(buffer)
writeTrackChunk2()



f.close()
    

import subprocess
subprocess.call(["/usr/local/bin/midicsv", fileName])
subprocess.call(["open", fileName])
print 60000000 / 120