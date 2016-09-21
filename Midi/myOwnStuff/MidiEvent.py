"""This application supports multiple tracks.  I'm thinking I should put a single channel on each track, but
might change that later"""

class Utils:
    @staticmethod
    def numberToFourBytes(number):
        array = [0]*4
        array[0] = (number>>24) & 0xff
        array[1] = (number>>16) & 0xff
        array[2] = (number>>8) & 0xff
        array[3] = number & 0xff
        print array
        return array
    
    @staticmethod
    def variBytes(number):
        array = [0]*4
        array[0] = (number>>24) & 0xff
        array[1] = (number>>16) & 0xff
        array[2] = (number>>8) & 0xff
        array[3] = number & 0xff
        # remove unnecessary (empty) bytes
        for i in range(3):
            if array[0] == 0: array.pop(0)
        return array
    
    @staticmethod
    def deltaTime(time):
        # times can be between 1 and 4 bytes    
        # split into 7 bit quantities (0 ... 127)
        array = [0]*4
        array[0] = time >> 21 & 0x7f
        array[1] = time >> 14 & 0x7f
        array[2] = time >>  7 & 0x7f
        array[3] = time & 0x7f
        # add continuation bits
        for i in range(3):
            if array[i] > 0: array[i] += 128    
        # remove unnecessary (empty) bytes
        for i in range(3):
            if array[0] == 0: array.pop(0)
        return array
    
    @staticmethod
    def timeDivision(code, format_):
        if format_ == "timeCodedBasedTime": raise("!!!!!! NOT IMPLEMENTED")
        if format_ == "metricalTime":
            array = [0, 0]
            array[0] = code >> 8 & 0xff
            array[1] = code & 0xff
        return array
    
class MidiEvent:
    def __init__(self):
        self.buffer = bytearray()
        self.channel = 0    # default channel
        
    def getBuffer(self):
        return self.buffer
    
    def addHeaderChunk(self, tracks = 1, tempo = 120):
        self.buffer.extend(map(ord,"MThd"))
        self.buffer.extend([0, 0, 0, 6])
        midiFormat = 1
        self.buffer.extend([0, midiFormat])
        self.buffer.extend([0, tracks])
        deltaTimeTicksPerQuarterNote = Utils.timeDivision(tempo * 4, "metricalTime")
        self.buffer.extend(deltaTimeTicksPerQuarterNote)

    def addTrackHeader(self):
        self.buffer.extend(map(ord, "MTrk"))
        self.reserveSpaceForTrackLength()
        self.setTimeSignature()
        self.setTempoAsMicrosecsPerQuarterNote()

        
    def reserveSpaceForTrackLength(self):
        self.buffer.extend([0,0,0,0])   # trackHeaderLength - calculated later
    
    def setDeltaTime(self, time):
        self.buffer.extend(Utils.deltaTime(time))

    def setTrackName(self, name):
        self.setDeltaTime(0)
        self.buffer.extend([0xFF, 0x03])
        self.buffer.append(len(name))
        self.buffer.extend(map(ord, name))

    def setCopyright(self, name):
        self.setDeltaTime(0)
        self.buffer.extend([0xFF, 0x02])
        self.buffer.append(len(name))
        self.buffer.extend(map(ord, name))

    def setTimeSignature(self):
        self.setDeltaTime(0)
        # time signature is 4/4
        # signature = numerator/2^denominator = 4/2^2 = 4/4
        bytesInSignature = 4
        numerator = 4
        denominator = 2
        # the header chunk defines deltaTimeTicksPerQuarterNote (e.g. 512)
        midiClocksPerTick = 24
        numberOfNotesPerTick = 8
        self.buffer.extend([0xFF, 0x58, bytesInSignature])
        self.buffer.extend([numerator, denominator, midiClocksPerTick, numberOfNotesPerTick]) 

    def setTempoAsMicrosecsPerQuarterNote(self, tempo = 500000):
        # Tempo = 60000000 / <tempo> beats per minute per quarter note
        # 60000000 / 500000 = 120  beats per minute per quarter note
        # n.b. 1 minute = 60,000,000 microSecs
        self.setDeltaTime(0)
        self.buffer.extend([0xFF, 0x51, 0x03])        
        self.buffer.extend(Utils.variBytes(tempo))
    
    def setInstrument(self, channel, voice, time = 0):
        self.channel = channel
        self.setDeltaTime(time)
        channel += 0xC0
        self.buffer.extend([channel, voice])

    def noteOn(self, note):
        status = 0x90 + self.channel
        self.buffer.extend([status, note, 0x7F])

    def noteOff(self, note):
        status = 0x80 + self.channel
        self.buffer.extend([status, note, 0x00])

    def noteOnOff(self, note, duration):
        self.setDeltaTime(0)
        self.noteOn(note)
        self.setDeltaTime(duration)
        self.noteOff(note)
        
    def endTrack(self):
        self.setDeltaTime(500)
        self.buffer.extend([0xFF ,0x2F ,0x00])
        # set track length
        self.buffer[4:8] = Utils.numberToFourBytes(len(self.buffer) - 8)
    
    def setTime(self, time):
        self.setDeltaTime(time)
        self.noteOff(0) # dummy operation
        


