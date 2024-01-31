
"""
MIDI Message Structure
There are three bytes of data per MIDI Message
[0x93, 0x3C, 0x7B]
The first is the status, which is a command
The second two are the payload message, which has extra parameters

The first nibble of the status is the function, the second is the channel

More info: https://www.cs.cmu.edu/~music/cmsip/readings/davids-midi-spec.htm
Some common ones:
0x8_ --> Note Off
0x9_ --> Note On
"""

import time
import rtmidi as midi
import random
import os

"""
Output Example:

midiOut = midi.MidiOut()
ports = midiOut.get_ports()

midiOut.open_port(1) # Opens My MIDI Keyboard
with midiOut:

    note_on = [0x94, 48, 100]
    note_off = [0x84, 48, 0]
    midiOut.send_message(note_on)
    time.sleep(1)
    midiOut.send_message(note_off)
    time.sleep(1)

del midiOut

"""




def clearChordList(chordNotes, characters):
    outStr = ''
    for note in sorted(chordNotes):
        outStr += characters[note - 21]

    chordNotes.clear()
    return outStr




maxChannel = 15
noteOnMessage = 144
deltaForChords = .05

midiIn = midi.MidiIn()
print(midiIn.get_ports())

midiIn.open_port(0)

print(midiIn.is_port_open())

listen = True
noteList = []
password = ''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[];:,.<>/?|~'
charList = list(chars)
random.seed(input("Seed for music: "))
random.shuffle(charList)

while listen:
    payload = midiIn.get_message()
    if (payload != None):
        message = payload[0]
        delta = payload[1]
        if (message[0] % noteOnMessage <= maxChannel and message[2] > 0):
            print(f'Note: {message[1]}\tDelta: {delta}')
            if (message[1] == 21):
                listen = False
            if (delta < deltaForChords):
                noteList.append(message[1])
            else:
                password += clearChordList(noteList, charList)
                noteList.append(message[1])
    else:
        time.sleep(.001)

print(password)
f = open("out.txt", 'a')
f.write(password + '\n')
f.close
        