#!/usr/bin/env python

import os
import signal
import subprocess
from sys import exit, version_info

import touchphat


try:
    os.environ['DISPLAY']
    print("""

Touch pHAT: App Launcher Example

A: Terminal
B: Browser
C: Idle
D: Dashboard 

Back: Logout
Enter: Shutdown

Press Ctrl+C to exit!
""")
except:
    print("""
No X display detected!
This example requires a full desktop
... exiting.
""")
    exit()


# shortcut to logout, reboot or shutdown using os.system
@touchphat.on_release('Back')
def handle_touch(event):
    os.system("lxsession-logout")

# simple use of os.system to launch a terminal window
@touchphat.on_release('A')
def handle_touch(event):
    os.system("x-terminal-emulator")
    print("New terminal")

# use of xdg-open to open in preferred browser application
@touchphat.on_release('B')
def handle_touch(event):
    os.system("xdg-open 'https://pimoroni.com' &")
    print("Browser launched")

# check for python version and use subprocess to track pid
@touchphat.on_release('C')
def handle_touch(event):
    if version_info[0] == 3:
        prog = "idle3"
    elif version_info[0] < 3:
        prog = "idle"

    running = subprocess.Popen([prog])
    print(prog.upper() + " launched with pid " + str(running.pid))

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
        print("Dashboard launched")

    except:
        print("Something went wrong!")

# shutdown with confirmation dialog via zenity with whiptail fallback
@touchphat.on_release('Enter')
def handle_touch(event):
    try:
        zencheck = subprocess.call(["which zenity"], stdout=subprocess.PIPE, shell=True)
        if zencheck != 1:
            subprocess.check_call(["zenity --question --text='Are you sure you want to shutdown?' 2> /dev/null"], shell=True)
            subprocess.check_call(["sudo shutdown +1"], shell=True)
        else:
            subprocess.check_call(["whiptail --yesno 'Are you sure you want to shutdown?' 10 50"], shell=True)
            subprocess.check_call(["sudo shutdown +1"], shell=True)
    except:
        print("Shutdown cancelled")

signal.pause()
