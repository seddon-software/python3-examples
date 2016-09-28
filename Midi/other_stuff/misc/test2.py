import time
import rtmidi
 
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
 
if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

midiout.send_message([0xC0, 0x41]) # (Alto Sax = 66 ==> coded 65 = 0x41)
midiout.send_message([0xC1, 0x00]) # (Piano = 1 ==> coded 0)
midiout.send_message([0xC9, 0x00]) # (Standard Drums Kit = 1 ==> coded 0)
t = 0.5 
for x in range(10):
    midiout.send_message([0x90, 0x48, 0x40]) # (Start sax C4, pitch = 72 = 0x48)
    midiout.send_message([0x91, 0x3C, 0x40]) # (Start piano C3, pitch = 60 = 0x3C)
    midiout.send_message([0x91, 0x43, 0x40]) # (Start piano G3, pitch = 67 = 0x43)
    midiout.send_message([0x91, 0x4C, 0x40]) # (Start piano E4, pitch = 76 = 0x4C)
    midiout.send_message([0x99, 0x23, 0x40]) # (Start Bass Drum = 35 = 0x23)
    time.sleep(t)
    midiout.send_message([0x80, 0x48, 0x00]) # (Stop sax C4, pitch = 72 = 0x48)
    midiout.send_message([0x89, 0x23, 0x00]) # (Stop Bass Drum = 35 = 0x23)
    midiout.send_message([0x90, 0x4A, 0x40]) # (Start sax D4, pitch = 74 = 0x4A)
    time.sleep(t)
    midiout.send_message([0x80, 0x4A, 0x00]) # (Stop sax D4, pitch = 74 = 0x4A)
    midiout.send_message([0x90, 0x4C, 0x40]) # (Start sax E4, pitch = 76 = 0x4C)
    midiout.send_message([0x99, 0x23, 0x40]) # (Start Bass Drum = 35 = 0x23)
    time.sleep(t)
    midiout.send_message([0x80, 0x4C, 0x00]) # (Stop sax E4, pitch = 76 = 0x4C)
    midiout.send_message([0x89, 0x23, 0x00]) # (Stop Bass Drum = 35 = 0x23)
    midiout.send_message([0x90, 0x4F, 0x40]) # (Start sax G4, pitch = 79 = 0x4F)
    time.sleep(0.1)
    midiout.send_message([0x80, 0x4F, 0x00]) # (Stop sax G4, pitch = 79 = 0x4F)
    midiout.send_message([0x81, 0x3C, 0x00]) # (Stop piano C3, pitch = 60 = 0x3C)
    midiout.send_message([0x81, 0x43, 0x00]) # (Stop piano G3, pitch = 67 = 0x43)
    midiout.send_message([0x81, 0x4C, 0x00]) # (Stop piano E4, pitch = 76 = 0x4C)
 
del midiout
