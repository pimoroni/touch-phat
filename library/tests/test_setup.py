import pytest


def test_setup(cap1xxx):
    import touchphat
    touchphat.setup()

    cap1xxx.Cap1166(i2c_addr=0x2c)._write_byte.assert_called_with(cap1xxx.R_LED_LINKING, 0b00000000)


def test_led(cap1xxx):
    import touchphat

    for pad, led in [('Back', 5), ('A', 4), ('B', 3), ('C', 2), ('D', 1), ('Enter', 0)]:
        touchphat.set_led(pad, False)
        cap1xxx.Cap1166(i2c_addr=0x2c).set_led_state.assert_called_with(
            led,
            False
        )