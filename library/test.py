import signal
import time

import touchphat


for pad in ['Back','A','B','C','D','Enter']:
    touchphat.set_led(pad, True)
    time.sleep(0.5)
    touchphat.set_led(pad, False)
    time.sleep(0.5)

@touchphat.on_touch(['Back','A','B','C','D','Enter'])
def handle_touch(event):
    print(event.name)

signal.pause()
