import re

class Pipeline:
    def __init__(self):
        self.notes = []
        self.durations = []
        
    def push(self, note, duration):
        notes = self.notes
        durations = self.durations
        notes.append(note)
        durations.append(duration)
        if len(notes) > 1:
            if durations[-1] != durations[-2]:
                theNotes = notes[:-1]
                theDuration = durations[-2]
                del notes[:-1]
                del durations[:-1]
                return theNotes, theDuration
        return None
    
    def finish(self):
        return self.notes, self.durations[0]

def convert(input_):
    notes = input_[0]
    duration = str(input_[1])
    if len(notes) > 1:
        chord = "{"
        for note in notes:
            chord += str(note) + ","
        chord += "}"
    else:
        chord = str(notes[0])
        
    pattern = re.compile(r"[']")
    chord = re.sub(pattern, "", chord)
    pattern = re.compile(r",}")
    chord = re.sub(pattern, "}", chord)

    return chord, duration
        
notes = [ 60, 61, 63, 68, 70, 72, 76, 77, 78, 79 ]
beats = [  0,  4,  4,  8,  8,  8, 12, 14, 14, 16 ]

p = Pipeline()
for pairs in zip(notes, beats):
    result = p.push(*pairs)
    if result != None: print convert(result)
print convert(p.finish())
