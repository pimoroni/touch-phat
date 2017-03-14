#!/usr/bin/env python

import signal
import time

import touchphat

print("""

Touch pHAT: Buttons Demo

Lights up each LED in turn, then detects your button presses.

Press a button to see the corresponding LED light up, and the name printed.

Press Ctrl+C to exit!

""")

for pad in ['Back','A','B','C','D','Enter']:
    touchphat.set_led(pad, True)
    time.sleep(0.1)
    touchphat.set_led(pad, False)
    time.sleep(0.1)

@touchphat.on_touch(['Back','A','B','C','D','Enter'])
def handle_touch(event):
    print(event.name)

signal.pause()
