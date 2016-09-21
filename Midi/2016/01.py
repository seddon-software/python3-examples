import rtmidi_python as rtmidi

vmidi_out = rtmidi.MidiOut()
vmidi_out.open_virtual_port('My Virtual MIDI Output Port')

vmidi_out.send_message([0x90, 48, 100]) # Note on
vmidi_out.send_message([176, 7, 100]) # Control Change - Volume 


import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
note_off = [0x80, 60, 0]
midiout.send_message(note_on)
time.sleep(0.5)
midiout.send_message(note_off)

del midiout
