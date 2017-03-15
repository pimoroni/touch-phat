#!/usr/bin/env python

import os
import signal
import subprocess
from sys import version_info

import touchphat

print("""

Touch pHAT: App Launcher Example

A: Terminal
B: Browser
C: Idle
D: Dashboard 

Press Ctrl+C to exit!

""")

# simple use of os.system to launch a terminal window
@touchphat.on_release('A')
def handle_touch(event):
    os.system("x-terminal-emulator")

# use of xdg-open to open in preferred browser application
@touchphat.on_release('B')
def handle_touch(event):
    os.system("xdg-open 'https://pimoroni.com' &")

# check for python version and use subprocess to track pid
@touchphat.on_release('C')
def handle_touch(event):
    if version_info[0] == 3:
        prog = "idle3"
    elif version_info[0] < 3:
        prog = "idle"

    running = subprocess.Popen([prog])
    print(prog + " pid " + str(running.pid))

# example installing a program if not available on system
@touchphat.on_release('D')
def handle_touch(event):
    try:
        dash = subprocess.call(["which pimoroni-dashboard"], stdout=subprocess.PIPE, shell=True)
        if dash != 1:
            subprocess.call(["x-terminal-emulator -e pimoroni-dashboard"], shell=True)
        else:
            print('Installing Dashboard')
            subprocess.call(["sudo apt-get install pimoroni"], shell=True)
            subprocess.call(["x-terminal-emulator -e pimoroni-dashboard"], shell=True)
            touchphat.led_off('D')
    except:
        print("Something went wrong!")

signal.pause()
