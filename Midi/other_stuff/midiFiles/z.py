import sys, os
import re
import subprocess

def process(notes, durations):
    n = 0
    notesList = []
    durationsList = []
    for note, duration in zip(notes, durations):
        notesList.append(note)
        durationsList.append(duration)
        if n % 8 == 0:
            print "m +=", notesList, "\\"
            print "\t", durationsList
            notesList = []
            durationsList = []
        n += 1
    print "m +=", notesList, "\\"
    print "\t", durationsList

def buildNoteOnList():
    pass

def buildNoteOffList():
    pass

def searchForMatchNoteOff():
    pass

def analyseFile(fileName):
    f = open(fileName, "r")
    notes = []
    durations = []
    previousTimeStamp = 0
    pattern = re.compile(r"[,]")
    
    for line in f:
        print line
        note = ""
        duration = ""
        line = re.sub(pattern, "", line)
        field = line.split()
        try:
            if field[2] == 'Note_on_c':
                note = field[4]
                timeStamp = field[1]
                duration = int(timeStamp) - int(previousTimeStamp)
                previousTimeStamp = timeStamp
        except Exception, e:
            print e
            sys.exit()
        if note != "":
            notes.append(note)
            durations.append(duration)
    f.close()
    process(notes, durations)

# base = sys.argv[1]
base = 10
print base
midicsv = "/usr/local/bin/midicsv"
midiIn = "{0}.mid".format(base)
midiOut = "{0}.txt".format(base)

cmd = "{0} {1}".format(midicsv, midiIn)
with open(midiOut, "w") as outfile:
    subprocess.call(cmd.split(), stdout=outfile)
analyseFile(midiOut)