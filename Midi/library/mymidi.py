import subprocess, sys
from midiutil.MidiFile import MIDIFile

"""
This class represents a MIDI track.  You can associate one Instrument with the track at
any given time.  Notes are sent to this object.  This class communicates directly with the MidiFile library.
"""
class Track():
    def __init__(self, MyMIDI, title, trackNo):
        self.MyMIDI = MyMIDI
        self.trackNo = trackNo
        self.time = 0
        self.trackName = title
        try:        
            self.MyMIDI.addTrackName(self.trackNo, self.time, self.trackName)
        except IndexError:
            print("Not enough tracks defined")
            sys.exit()
        self.pitchShift = 0
    
    def setTempo(self, tempo):
        self.MyMIDI.addTempo(self.trackNo, self.time, tempo)

    def setInstrument(self, instrument, channel, volume = 127, pitchShift = 0):
        if isinstance(instrument, str):
            try:
                instrumentCode = VoiceToNumber[instrument] - 1
            except Exception as e:
                print("not a valid instrument: {0}".format(e))
                sys.exit()
        else:
            raise Exception("illegal instrument {0}".format(instrument))
        self.pitchShift = pitchShift
        self.currentInstrument = Instrument(instrumentCode, channel, volume)
        self.MyMIDI.addProgramChange(self.trackNo, channel, self.time, instrumentCode)
        return self.currentInstrument

    """
    notes are in range 1 .. 127
    note = 0 is interpreted as a rest
    """
    def addNote(self, notes, duration = 1):
        trackNo = self.trackNo
        channel = self.currentInstrument.getChannel()
        time = self.time
        volume = self.currentInstrument.getVolume()
        if isinstance(notes, set):
            for note in notes:
                note += self.pitchShift
                self.MyMIDI.addNote(trackNo, channel, note, time, duration, volume)
        elif isinstance(notes, int):
            note = notes
            if note != 0:
                note += self.pitchShift
                self.MyMIDI.addNote(trackNo, channel, note, time, duration, volume)
            else:   # rest
                self.MyMIDI.addNote(trackNo, channel, note, time, duration, 0)                
        else:
            message = "malformed notes {0}".format(notes)
            raise Exception(message)            
        self.time += duration

    def __iadd__(self, rhs):
        if isinstance(rhs, Instrument.Score):
            for item in rhs.get():
                (note, duration) = item
                self.addNote(note, duration)            
        elif isinstance(rhs, set):
            raise("Not implemented yet")
        elif isinstance(rhs, tuple) or isinstance(rhs, list):
            if len(rhs) == 2:
                notes = Instrument.Notes(*rhs[0])
                durations = Instrument.Durations(*rhs[1])
                score = Instrument.Score(notes, durations)
                self += score
        else:
            message = "malformed score {0}".format(rhs)
            raise Exception(message)
        return self

"""
This class is the container for a set of Track objects.  You can set the tempo for all the MIDI tracks from here
(you can set different tempos on different tracks.  The class contains the play method which launches the default
MIDI player and saves the MIDI file on disk.
"""        
class Tracks:
    def __init__(self, name, tracks):
        self.name = name
        self.tracks = []
        self.MyMIDI = MIDIFile(tracks)

    def addTrack(self, title):
        trackNo = len(self.tracks)
        track = Track(self.MyMIDI, title, trackNo)
        self.tracks.append(track)
        return track
    
    def setTempo(self, tempo = 120):
        if len(self.tracks) == 0:
            print("create the tracks before you set the tempo")
            sys.exit()
        for track in self.tracks:
            track.setTempo(tempo)
    
    def getTracks(self):
        return self.tracks
    
    def play(self, debug = False):
        outFileName = "newMidiFiles/" + self.name + ".mid"
        binfile = open(outFileName, 'wb')
        self.MyMIDI.writeFile(binfile)
        binfile.close()
        cmd = "open " + outFileName
        subprocess.call(cmd.split())
        if debug: subprocess.call(["/usr/local/bin/midicsv", outFileName])

"""
This class represents and instrument.  It uses Notes and Durations wrapped up in a Score.
"""
class Instrument:
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
            self.score = list(zip(notes.get(), durations.get()))

        def get(self):
            return self.score

    def __init__(self, program, channel, volume, tempo = 120):
        self.channel = channel
        self.program = program
        self.tempo = tempo
        self.time = 0
        self.track = 0  
        self.volume = volume

    def getChannel(self):
        return self.channel
    
    def setVolume(self, volume):
        self.volume = volume
        
    def getVolume(self):
        return self.volume
    



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

NumberToVoice = {
1  : "Acoustic Grand Piano",
2  : "Bright Acoustic Piano",
3  : "Electric Grand Piano",
4  : "Honky-tonk Piano",
5  : "Electric Piano 1",
6  : "Electric Piano 2",
7  : "Harpsichord",
8  : "Clavinet",
9  : "Celesta",
10  : "Glockenspiel",
11  : "Music Box",
12  : "Vibraphone",
13  : "Marimba",
14  : "Xylophone",
15  : "Tubular Bells",
16  : "Dulcimer",
17  : "Drawbar Organ",
18  : "Percussive Organ",
19  : "Rock Organ",
20  : "Church Organ",
21  : "Reed Organ",
22  : "Accordion",
23  : "Harmonica",
24  : "Tango Accordion",
25  : "Acoustic Guitar (nylon)",
26  : "Acoustic Guitar (steel)",
27  : "Electric Guitar (jazz)",
28  : "Electric Guitar (clean)",
29  : "Electric Guitar (muted)",
30  : "Overdriven Guitar",
31  : "Distortion Guitar",
32  : "Guitar Harmonics",
33  : "Acoustic Bass",
34  : "Electric Bass (finger)",
35  : "Electric Bass (pick)",
36  : "Fretless Bass",
37  : "Slap Bass 1",
38  : "Slap Bass 2",
39  : "Synth Bass 1",
40  : "Synth Bass 2",
41  : "Violin",
42  : "Viola",
43  : "Cello",
44  : "Contrabass",
45  : "Tremolo Strings",
46  : "Pizzicato Strings",
47  : "Orchestral Harp",
48  : "Timpani",
49  : "String Ensemble 1",
50  : "String Ensemble 2",
51  : "Synth Strings 1",
52  : "Synth Strings 2",
53  : "Choir Aahs",
54  : "Voice Oohs",
55  : "Synth Choir",
56  : "Orchestra Hit",
57  : "Trumpet",
58  : "Trombone",
59  : "Tuba",
60  : "Muted Trumpet",
61  : "French Horn",
62  : "Brass Section",
63  : "Synth Brass 1",
64  : "Synth Brass 2",
65  : "Soprano Sax",
66  : "Alto Sax",
67  : "Tenor Sax",
68  : "Baritone Sax",
69  : "Oboe",
70  : "English Horn",
71  : "Bassoon",
72  : "Clarinet",
73  : "Piccolo",
74  : "Flute",
75  : "Recorder",
76  : "Pan Flute",
77  : "Blown bottle",
78  : "Shakuhachi",
79  : "Whistle",
80  : "Ocarina",
81  : "Lead 1 (square)",
82  : "Lead 2 (sawtooth)",
83  : "Lead 3 (calliope)",
84  : "Lead 4 chiff",
85  : "Lead 5 (charang)",
86  : "Lead 6 (voice)",
87  : "Lead 7 (fifths)",
88  : "Lead 8 (bass + lead)",
89  : "Pad 1 (new age)",
90  : "Pad 2 (warm)",
91  : "Pad 3 (polysynth)",
92  : "Pad 4 (choir)",
93  : "Pad 5 (bowed)",
94  : "Pad 6 (metallic)",
95  : "Pad 7 (halo)",
96  : "Pad 8 (sweep)",
97  : "FX 1 (rain)",
98  : "FX 2 (soundtrack)",
99  : "FX 3 (crystal)",
100  : "FX 4 (atmosphere)",
101  : "FX 5 (brightness)",
102  : "FX 6 (goblins)",
103  : "FX 7 (echoes)",
104  : "FX 8 (sci-fi)",
105  : "Sitar",
106  : "Banjo",
107  : "Shamisen",
108  : "Koto",
109  : "Kalimba",
110  : "Bagpipe",
111  : "Fiddle",
112  : "Shanai",
113  : "Tinkle Bell",
114  : "Agogo",
115  : "Steel Drums",
116  : "Woodblock",
117  : "Taiko Drum",
118  : "Melodic Tom",
119  : "Synth Drum",
120  : "Reverse Cymbal",
121  : "Guitar Fret Noise",
122  : "Breath Noise",
123  : "Seashore",
124  : "Bird Tweet",
125  : "Telephone Ring",
126  : "Helicopter",
127  : "Applause",
128  : "Gunshot",
}
