![Touch pHAT](touchphat-logo.png)
https://shop.pimoroni.com/products/touch-phat

[![Build Status](https://shields.io/github/workflow/status/pimoroni/touch-phat/Python%20Tests.svg)](https://github.com/pimoroni/touch-phat/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/touch-phat/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/touch-phat?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/touchphat.svg)](https://pypi.python.org/pypi/touchphat)
[![Python Versions](https://img.shields.io/pypi/pyversions/touchphat.svg)](https://pypi.python.org/pypi/touchphat)

Touch pHAT is a simple add-on for your Pi or Pi Zero that includes 6 touch sensitive pads. Use it to add touch control to your projects.

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your Touch pHAT
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/touchphat | bash
```

Alternatively, on Raspbian, you can download the `pimoroni-dashboard` and install your product by browsing to the relevant entry:

```bash
sudo apt-get install pimoroni
```
(you will find the Dashboard under 'Accessories' too, in the Pi menu - or just run `pimoroni-dashboard` at the command line)

If you choose to download examples you'll find them in `/home/pi/Pimoroni/touchphat/`.

### Manual install:

You'll need to enable i2c:

```
sudo raspi-config nonint do_i2c 0
```

#### Library install for Python 3:

```bash
sudo python3 -m pip install touchphat
```

#### Library install for Python 2:

```bash
sudo python2 -m pip install touchphat
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python3 setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/touch-phat
* Function reference - http://docs.pimoroni.com/touchphat/
* GPIO Pinout - https://pinout.xyz/pinout/touch_phat
* Get help - http://forums.pimoroni.com/c/support

# Changelog
0.0.2
-----

* Enhancement: Migrate to setup.cfg, linting and tidyup
* Enhancement: Defer setup to avoid import side-effects
* BugFix: ValueError now returned on invalid pad number or name, instead of TypeError

0.0.1
-----

* Initial release

