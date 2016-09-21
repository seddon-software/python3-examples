"""
visit http://www.midi.org/techspecs/midimessages.php for MIDI codes
"""

"""
The CLP-150 must be setup such that each MidiInChannel (1-16) is set to SONG and
the SONG-KEYBOARD slider is not on the extreme right (KEYBOARD) or you will not be able to hear anything
Other settings are at default levels

Bank Change message appears to be:
    0xBn, 0x00, 0xZZ
wher n is channel and ZZ is the bank number
"""

import sys, time, os.path
import rtmidi

def setup():

    available_ports = midiout.get_ports()
    
    if available_ports:
        midiout.open_port(0)
        print "sending midi to the piano"
        for channel in range(1, 16+1):
            reset = [0xB0 + channel - 1, 0x7B, 0]            
            midiout.send_message(reset)
    else:
        print "No available MIDI ports - are you connected to the piano?"

    if os.path.isfile("lock"):
        os.remove("lock")
        print "reseting controllers - try again"
        sys.exit()

midiout = rtmidi.MidiOut()
# midiout.send_message([0xB0, 0x00, 0x00])
# midiout.send_message([0xB1, 0x00, 0x00])
# midiout.send_message([0xB2, 0x00, 0x00])
setup()

class Midi:
    class Sequence:
        sequence = []
        @staticmethod
        def addMessage(beat, message):
            Midi.Sequence.sequence.append([beat, message])
    
        @staticmethod
        def sorted():
            return sorted(Midi.Sequence.sequence, key=lambda x: x[0])
    
    def __init__(self, tempo, debug = False):
        self.tempo = tempo
        self.debug = debug
        self.channels = []
            
    def dump(self):
        for [beat, midiMessage] in Midi.Sequence.sorted():
            print beat, "[", 
            for byte_ in midiMessage:
                print "{0:02x}".format(byte_),
            print "]"
    def setTempo(self, tempo):
        self.tempo = tempo       
        
    def printMessage(self, beat, message): 
        print beat,
        for byte_ in message:
            print "{0:X}".format(byte_),
        print

    def play(self):
        previousBeat = 0
        # create lock file to indicate we are sending midi messages
        # in case we get interrupted half way through
        # otherwise notes will not swich off
        open("lock", "w")
        for [beat, midiMessage] in Midi.Sequence.sorted():
            # send message
            midiout.send_message(midiMessage)
            if self.debug: self.printMessage(beat, midiMessage)
            # wait for next event
            if previousBeat != beat:
                # duration = 1 quarter_beats (tempo = 120 qb/min or 2 qb/sec) so 1 qb = 1/2 sec
                duration = beat - previousBeat
                quarterBeatsPerSec = self.tempo / 60.0
                time.sleep(duration/quarterBeatsPerSec)
                previousBeat = beat
        # remove lock file to indicate we have finished sending midi messages
        os.remove("lock")
    
    def getChannels(self):
        return self.channels
    
    def createChannel(self, instrument, channel, volume = 127, pitchShift = 0):
        newChannel = Channel(instrument, channel, volume, pitchShift)
        self.channels.append(newChannel)
        return newChannel

class Channel:
    class Notes:
        def __init__(self, *notes):
            self.notes = notes
        def get(self):
            return self.notes
    
    class Durations:
        def __init__(self, *durations):
            self.durations = durations
        def get(self):
            return self.durations
    
    class Score:
        def __init__(self, notes, durations):
            self.score = zip(notes.get(), durations.get())

        def get(self):
            return self.score
        
    def __init__(self, instrument, channel, volume, pitchShift):
        try:
            instrument = self.__class__.VoiceToNumber[instrument] - 1
        except KeyError:
            print "{0} is not a valid instrument".format(instrument)
            sys.exit()
        self.check(channel, 1, 16)
        self.instrument = instrument
        self.channel = channel
        self.beat = 0
        self.velocity = volume
        self.pitchShift = pitchShift
        self.programChange(channel, instrument)
    
    def __iadd__(self, rhs):
        if isinstance(rhs, self.__class__.Score):
            for item in rhs.get():
                (note, duration) = item
                self.addNote(note, duration)            
        elif isinstance(rhs, tuple) or isinstance(rhs, list):
            if len(rhs) == 2:
                notes = self.__class__.Notes(*rhs[0])
                durations = self.__class__.Durations(*rhs[1])
                score = self.__class__.Score(notes, durations)
                self += score
        else:
            raise Exception("malformed score {0}".format(rhs))
        return self
    
    def addNote(self, notes, duration):
        channel = self.channel
        velocity = self.velocity

        if isinstance(notes, int):
            notes = set([notes])
        if isinstance(notes, set):  # chord
            for note in notes:
                if note != 0:
                    note = note + self.pitchShift
                    self.noteOn(channel = channel, note = note, velocity = velocity)
                else:
                    self.noteOn(channel = channel, note = note, velocity = 0)                    
            self.beat += duration
            for note in notes:
                if note != 0:
                    note = note + self.pitchShift
                    self.noteOff(channel = channel, note = note, velocity = 0)
                else:
                    self.noteOff(channel = channel, note = note, velocity = 0)                    
        else:
            raise Exception("malformed notes {0}".format(notes))                    
        
    def check(self, value, lowerBound, upperBound):
        if not isinstance(value, int): raise Exception("{0} must be an integer".format(value))
        if value < lowerBound: raise Exception("{0} must be >= {1}".format(value, lowerBound))
        if value > upperBound: raise Exception("{0} must be <= {1}".format(value, upperBound))

    def noteOff(self, channel, note, velocity):
        self.check(channel, 1, 16)
        self.check(note, 0, 127)
        self.check(velocity, 0, 127)
        byte1 = 0x80 + channel - 1
        Midi.Sequence.addMessage(self.beat, [byte1, note, 127])

    def noteOn(self, channel, note, velocity):
        self.check(channel, 1, 16)
        self.check(note, 0, 127)
        self.check(velocity, 0, 127)
        byte1 = 0x90 + channel - 1
        Midi.Sequence.addMessage(self.beat, [byte1, note, velocity])
    
    def polyphonicAftertouch(self, channel, note, pressure):
        self.check(channel, 1, 16)
        self.check(note, 0, 127)
        self.check(pressure, 0, 127)
        byte1 = 0xA0 + channel - 1
        Midi.Sequence.addMessage(self.beat, [byte1, note, pressure])

    def programChange(self, channel, program):
        self.check(channel, 1, 16)
        self.check(program, 0, 127)
        byte1 = 0xC0 + channel - 1
        Midi.Sequence.addMessage(self.beat, [byte1, program])
    
    def cycleThroughInstruments(self, lower, upper):
        for instrument in range(lower, upper + 1):
            self.programChange(self.channel, instrument)
            self.addNote(60, 1)
            print instrument
        
    VoiceToNumber = {
        "Acoustic Grand Piano" : 1 ,
        "Bright Acoustic Piano" : 2 ,
        "Electric Grand Piano" : 3 ,
        "Honky-tonk Piano" : 4 ,
        "Electric Piano 1" : 5 ,
        "Electric Piano 2" : 6 ,
        "Harpsichord" : 7 ,
        "Clavinet" : 8 ,
        "Celesta" : 9 ,
        "Glockenspiel" : 10 ,
        "Music Box" : 11 ,
        "Vibraphone" : 12 ,
        "Marimba" : 13 ,
        "Xylophone" : 14 ,
        "Tubular Bells" : 15 ,
        "Dulcimer" : 16 ,
        "Drawbar Organ" : 17 ,
        "Percussive Organ" : 18 ,
        "Rock Organ" : 19 ,
        "Church Organ" : 20 ,
        "Reed Organ" : 21 ,
        "Accordion" : 22 ,
        "Harmonica" : 23 ,
        "Tango Accordion" : 24 ,
        "Acoustic Guitar (nylon)" : 25 ,
        "Acoustic Guitar (steel)" : 26 ,
        "Electric Guitar (jazz)" : 27 ,
        "Electric Guitar (clean)" : 28 ,
        "Electric Guitar (muted)" : 29 ,
        "Overdriven Guitar" : 30 ,
        "Distortion Guitar" : 31 ,
        "Guitar Harmonics" : 32 ,
        "Acoustic Bass" : 33 ,
        "Electric Bass (finger)" : 34 ,
        "Electric Bass (pick)" : 35 ,
        "Fretless Bass" : 36 ,
        "Slap Bass 1" : 37 ,
        "Slap Bass 2" : 38 ,
        "Synth Bass 1" : 39 ,
        "Synth Bass 2" : 40 ,
        "Violin" : 41 ,
        "Viola" : 42 ,
        "Cello" : 43 ,
        "Contrabass" : 44 ,
        "Tremolo Strings" : 45 ,
        "Pizzicato Strings" : 46 ,
        "Orchestral Harp" : 47 ,
        "Timpani" : 48 ,
        "String Ensemble 1" : 49 ,
        "String Ensemble 2" : 50 ,
        "Synth Strings 1" : 51 ,
        "Synth Strings 2" : 52 ,
        "Choir Aahs" : 53 ,
        "Voice Oohs" : 54 ,
        "Synth Choir" : 55 ,
        "Orchestra Hit" : 56 ,
        "Trumpet" : 57 ,
        "Trombone" : 58 ,
        "Tuba" : 59 ,
        "Muted Trumpet" : 60 ,
        "French Horn" : 61 ,
        "Brass Section" : 62 ,
        "Synth Brass 1" : 63 ,
        "Synth Brass 2" : 64 ,
        "Soprano Sax" : 65 ,
        "Alto Sax" : 66 ,
        "Tenor Sax" : 67 ,
        "Baritone Sax" : 68 ,
        "Oboe" : 69 ,
        "English Horn" : 70 ,
        "Bassoon" : 71 ,
        "Clarinet" : 72 ,
        "Piccolo" : 73 ,
        "Flute" : 74 ,
        "Recorder" : 75 ,
        "Pan Flute" : 76 ,
        "Blown bottle" : 77 ,
        "Shakuhachi" : 78 ,
        "Whistle" : 79 ,
        "Ocarina" : 80 ,
        "Lead 1 (square)" : 81 ,
        "Lead 2 (sawtooth)" : 82 ,
        "Lead 3 (calliope)" : 83 ,
        "Lead 4 chiff" : 84 ,
        "Lead 5 (charang)" : 85 ,
        "Lead 6 (voice)" : 86 ,
        "Lead 7 (fifths)" : 87 ,
        "Lead 8 (bass + lead)" : 88 ,
        "Pad 1 (new age)" : 89 ,
        "Pad 2 (warm)" : 90 ,
        "Pad 3 (polysynth)" : 91 ,
        "Pad 4 (choir)" : 92 ,
        "Pad 5 (bowed)" : 93 ,
        "Pad 6 (metallic)" : 94 ,
        "Pad 7 (halo)" : 95 ,
        "Pad 8 (sweep)" : 96 ,
        "FX 1 (rain)" : 97 ,
        "FX 2 (soundtrack)" : 98 ,
        "FX 3 (crystal)" : 99 ,
        "FX 4 (atmosphere)" : 100 ,
        "FX 5 (brightness)" : 101 ,
        "FX 6 (goblins)" : 102 ,
        "FX 7 (echoes)" : 103 ,
        "FX 8 (sci-fi)" : 104 ,
        "Sitar" : 105 ,
        "Banjo" : 106 ,
        "Shamisen" : 107 ,
        "Koto" : 108 ,
        "Kalimba" : 109 ,
        "Bagpipe" : 110 ,
        "Fiddle" : 111 ,
        "Shanai" : 112 ,
        "Tinkle Bell" : 113 ,
        "Agogo" : 114 ,
        "Steel Drums" : 115 ,
        "Woodblock" : 116 ,
        "Taiko Drum" : 117 ,
        "Melodic Tom" : 118 ,
        "Synth Drum" : 119 ,
        "Reverse Cymbal" : 120 ,
        "Guitar Fret Noise" : 121 ,
        "Breath Noise" : 122 ,
        "Seashore" : 123 ,
        "Bird Tweet" : 124 ,
        "Telephone Ring" : 125 ,
        "Helicopter" : 126 ,
        "Applause" : 127 ,
        "Gunshot" : 128 
    }
