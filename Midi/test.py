import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")
# C0, C1, C2

def send(channel, message):
    global middiout
    message[0] += channel - 1
    midiout.send_message(message)

def progChange(channel, instrument):
    byte0 = 0xC0 + channel - 1
    byte1 = instrument
    midiout.send_message([byte0, byte1])
    
note_on = [0x90, 60, 112]
note_off = [0x80, 60, 0]

for i in range(1,10):
    print i
    ch = 2
    time.sleep(0.5)
    progChange(ch, i)
    time.sleep(0.5)
    send(ch, note_on)
    time.sleep(1.0)
    send(ch, note_off)

del midiout
