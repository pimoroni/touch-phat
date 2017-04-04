#!/usr/bin/env python

import mock
import sys
import signal
import time

sys.modules['cap1xxx'] = mock.Mock()

import touchphat

def assert_raises(action, expect, message):
    try:
        action()
    except expect:
        return
    except Exception as e:
        print(message)
        raise e

def test_handler(evt):
    pass

assert hasattr(touchphat, "__version__") == True, "Touch pHAT module should include a __version__ attribute"

print("Testing Touch pHAT version: {}".format(touchphat.__version__))

assert touchphat.NAMES == ['Back', 'A', 'B', 'C', 'D', 'Enter'], "NAMES should be: 'Back', 'A', 'B', 'C', 'D', 'Enter'"

assert touchphat.NUMMAP == [1, 2, 3, 4, 5, 6], "NUMMAP should be a list of numbers from 1 to 6"

assert_raises(lambda: touchphat.set_led(0, True), ValueError, "touchpad.set_led(0, True) should raise ValueError")
assert_raises(lambda: touchphat.on_touch(0, handler=test_handler), ValueError, "touchphat.on_touch(0, ...) should raise ValueError")
assert_raises(lambda: touchphat.on_release(0, handler=test_handler), ValueError, "touchphat.on_release(0, ...) shoudl raise ValueError")

print("Passed!")
