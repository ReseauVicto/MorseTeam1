#!/usr/bin/env python

import gpiozero import LED

led = LED(17)

def A():
    led.On()
