import re

instruments = ["Harp", "Sweep"]
notewothyFile = "02.nw"
pitchChange = 60

def generateInstrumentPattern(instruments):
    firstInstrument = instruments.pop(0)
    pattern = r"\+({0}".format(firstInstrument)    
    for instrument in instruments:
        pattern += r"|{0}".format(instrument)
    pattern += ")"
    return re.compile(pattern)   

def readInputFile(fileName):
    rawList = ""
    with open(fileName, "r") as infile:
        rawList = rawList + str(infile.read())
    pattern = re.compile(r"([{].*?[}]|.+?)\s+", flags = re.MULTILINE)
    rawList = re.findall(pattern, rawList)
    return rawList

def parse(original, pattern, token):
    match = pattern.match(token)
    if match != None:
        return match.group(1)
    else:
        return original 

def main():
    notes = []
    durations = []
    duration = note = 1
    triple = tempo = dot = rest = None
    durationPattern = re.compile(r"\[(\d+)\]")
    notePattern = re.compile(r"(\d+)")
    triplePattern = re.compile(r"\+(triple)")
    tempoPattern = re.compile(r"\+Tempo(\d+)")
    dotPattern = re.compile(r"\+(dot)")
    restPattern = re.compile(r"\+(rest)")
    chordPattern = re.compile(r"\{(.*)\}")
    instrumentPattern = generateInstrumentPattern(instruments)
    rawList = readInputFile(notewothyFile)
    for token in rawList:
        note = int(parse(-1, notePattern, token))
        duration = int(parse(-1, durationPattern, token))
        if duration != -1: 
            inverseDuration = 64 / duration
        triple = parse(None, triplePattern, token)
        tempo = parse(None, tempoPattern, token)
        dot = parse(None, dotPattern, token)
        rest = parse(None, restPattern, token)
        instrument = parse(None, instrumentPattern, token)
        chord = parse(None, chordPattern, token)
        if triple:
            durations[-3] = durations[-3] * 3
            durations[-2] = durations[-2] * 3
            durations[-1] = durations[-1] * 3
        if rest:
            note = -pitchChange
        if note != -1:
            notes.append(pitchChange + note)
            durations.append(inverseDuration)
        if tempo:
            print "TEMPO: {0}".format(tempo) 
        if dot:
            inverseDuration = int( inverseDuration * 1.5 )
        if instrument:
            printScore(notes, durations)
            print "CHANNEL: {0}".format(instrument)
            notes = []
            durations = []
        if chord:
            chord = chord.split()
            note = chord.pop(0)
            note = int(note) + pitchChange
            s = "{" + str(note)
            note = int(note) + pitchChange
            for note in chord:
                note = int(note) + pitchChange
                s += "," + str(note)
            s += "}"
            notes.append(s)
            durations.append(inverseDuration)
    printScore(notes, durations)

def printLists(notesList, durationsList):
    if notesList: 
        print "\tm += [{0}".format(notesList.pop(0)),
        for note in notesList:
            print ",{0}".format(note),
        print "], \\".format(notesList)
    if durationsList: print "\t     {0}".format(durationsList)
    
''' print out notes and durations, 8 to a line '''
def printScore(notes, durations):
    notesList = []
    durationsList = []
    for i, [note, duration] in enumerate(zip(notes, durations)):
        if i % 8 == 0:
            printLists(notesList, durationsList)
            notesList = [-1]*8
            durationsList = [-1]*8
        notesList[i % 8] = note
        durationsList[i % 8] = duration
    printLists(notesList, durationsList)

main()
