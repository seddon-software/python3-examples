import sys, re
import subprocess, StringIO, numpy



class Pipeline:
    def __init__(self):
        self.notes = []
        self.beats = []
        
    @staticmethod
    def convertNotesToString(notes): 
        if len(notes) == 1:
            return notes[0]
        else:
            s = ",".join(notes)
            return "{" + s + "}"

    def push(self, note, beat):
        note = str(note)
        notes = self.notes
        beats = self.beats
        notes.append(note)
        beats.append(beat)
        if len(notes) > 1:
            if beats[-1] != beats[-2]:
                theNotes = notes[:-1]
                del notes[:-1]
                del beats[:-1]
                return Pipeline.convertNotesToString(theNotes)
        return None
    
    def finish(self):
        return self.notes, self.beats[0]


''' print out notes and durations, 8 to a line '''
def process(channel, notes, durations, beats, output):
    n = 1
    notesList = []
    durationsList = []
    p = Pipeline()
    for note, duration, beat in zip(notes, durations, beats):
        chord = p.push(note, beat)
        if chord != None:
            notesList.append(chord)
            durationsList.append(duration)
            if n % 8 == 0:
                notesList = ",".join(notesList)
                print >>output, "\tm += [{0}], \\".format(notesList)
                print >>output, "\t\t", durationsList
                notesList = []
                durationsList = []
            n += 1

    notesList = "".join(notesList)
    print >>output, "\tm += [{0}], \\".format(notesList)
    print >>output, "\t\t{0}".format(durationsList)
    return output

''' read the input file and convert it to a list of midi events'''
def convertFileToListOfMidiEvents(fileName):
    f = open(fileName, "r")
    rawList = []
    pattern = re.compile(r"[,\n]")
    
    for line in f:
        line = re.sub(pattern, "", line)
        fields = line.split()
        for i in range(0, len(fields)):
            try:    # to convert to int
                fields[i] = int(fields[i])
            except:
                pass # no conversion possible
            
        rawList.append(fields)
    f.close()
    return rawList


def buildNoteOnList(rawList, selectedChannel):
    newList = []
    for line in rawList:
        if len(line) == 6:
            channel = line[0]
            key = line[2]
            volume = line[5]
            if (channel == selectedChannel) and (key == 'Note_on_c') and (volume > 0):
                newList.append(line)
    return None if len(newList) == 0 else newList 

def buildNoteOffList(rawList, selectedChannel):
    newList = []
    for line in rawList:
        if len(line) == 6:
            channel = line[0]
            key = line[2]
            volume = line[5]
            if (channel == selectedChannel) and (key == 'Note_on_c') and (volume == 0):
                newList.append(line)
            if (channel == selectedChannel) and (key == 'Note_off_c'):
                newList.append(line)
    return None if len(newList) == 0 else newList

def appendTimings(noteOnList, noteOffList, modifiedDurations):
    for line in noteOnList:
        tickOn = line[1]
        noteOn = line[4]
        tickOff = searchForMatchNoteOff(tickOn, noteOn, noteOffList)
        duration = tickOff - tickOn if tickOff != None else None
        for key in modifiedDurations:
            replacement = modifiedDurations[key]
            if key == duration: duration = replacement
        line.append(duration)

def searchForMatchNoteOff(tickOn, noteOn, noteOffList):
    for line in noteOffList:
        tickOff = line[1]
        noteOff = line[4]
        if (noteOff == noteOn) and (tickOff > tickOn):
            return tickOff
    print "no matching note off for {0} at {1}".format(noteOn, tickOn)
    return None     # shouldn't happen

def extractNotesAndDurations(noteOnList):
    notes = []
    durations = []
    beats = []
    for line in noteOnList:
        beat = line[1]
        note = line[4]
        duration = line[6]
        notes.append(note)
        durations.append(duration)
        beats.append(beat)
    return notes, durations, beats

def modifyDuration(duration, durationFudgeFactor, durationUnit, modifiedDurations = {}):
    for key in modifiedDurations:
        replacement = modifiedDurations[key]
        if key == duration: duration = replacement
    return duration

    
def printStatistics(noteOnList, noteOffList, channel):
    print "======================== Channel {0} data ========================".format(channel)    
    print "number of note_on = {0}".format(len(noteOnList))
    print "number of note_off = {0}".format(len(noteOffList))
    
    durations = []
    for line in noteOnList:
        duration = line[6]
        durations.append(duration)
    durations = list(set(durations))
    durations.sort()
    differences = numpy.diff(durations)
    print "durations, differences", durations, differences

def createRawList(base):
    print "converting {0}.mid".format(base)
    midicsv = "/usr/local/bin/midicsv"
    midiIn = "{0}.mid".format(base)
    midiOut = "{0}.txt".format(base)
    
    cmd = "{0} {1}".format(midicsv, midiIn)
    with open(midiOut, "w") as outfile:
        subprocess.call(cmd.split(), stdout=outfile)
    rawList = convertFileToListOfMidiEvents(midiOut)
    return rawList

def printList(rawList):
    for entry in rawList:
        print entry

def main():
#     if len(sys.argv) != 2:
#         print "useage: python midiFile.mid"
#         sys.exit()
#     midiFileList = str.split(sys.argv[1], ".")
#     midiFileBase = midiFileList[0] 

    midiFileBase = '17'
    replacementDurations = {94:1, 160:2, 190:4, 352:8} 
    
    noteOnList = [ ]
    noteOffList = [ ]
    output = StringIO.StringIO()

    rawList = createRawList(midiFileBase)
    printList(rawList)
    for channel in range(1, 16+1):
        noteOnList = buildNoteOnList(rawList, channel)
        noteOffList = buildNoteOffList(rawList, channel)
        
        if noteOnList != None:
            appendTimings(noteOnList, noteOffList, replacementDurations)
            printStatistics(noteOnList, noteOffList, channel)
            notes, durations, beats = extractNotesAndDurations(noteOnList)
            output = process(channel, notes, durations, beats, output)
            print output.getvalue()
            

main()
