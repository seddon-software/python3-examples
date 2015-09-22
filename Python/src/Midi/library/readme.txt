The Python library code for MIDIUtil is at:
	/Users/seddon/work/MIDIUtil-0.89
There is only one source file:
	/Users/seddon/work/MIDIUtil-0.89/src/midiutil/MidiFile.py

The fundamental class and key methods are:

class MIDIFile:
    addNote(track, channel, pitch,time,duration,volume)
    addTrackName(track, time, trackName)
    addTempo(track, time, tempo)
    addProgramChange(track, channel, time, program)
    addControllerEvent(track, channel, time, eventType, parameter1)
    changeNoteTuning(track, tunings, sysExChannel=0x7F, realTime=False, tuningProgam=0)
    writeFile(fileHandle)
    addSysEx(track, time, manID, payload)
    addUniversalSysEx(track,  time,code, subcode, payload, sysExChannel=0x7F,  realTime=False)
    shiftTracks(offset=0)

Basically:
    addNote				- add note
    addTrackName		- descriptive
    addTempo			- set tempo
    addProgramChange	- set instrument
    addControllerEvent	- various controls (e.g. volume, pedal)
    changeNoteTuning	- ??
    writeFile			- save file
    addSysEx			- ??
    addUniversalSysEx	- ??
    shiftTracks			- ??
    