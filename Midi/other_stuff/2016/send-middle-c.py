import time
import rtmidi


def play(note):
    note_on = [0x90, note, 112] # channel 1, middle C, velocity 112
    note_off = [0x80, note, 0]
    midiout.send_message(note_on)
    time.sleep(0.5)
    midiout.send_message(note_off)

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print(available_ports)
if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")


play(60)
play(62)
play(60)


del midiout
