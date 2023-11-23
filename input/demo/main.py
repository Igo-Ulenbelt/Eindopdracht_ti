from machine import Pin
import time

led_pin = Pin(20, Pin.OUT)
switch_pin_1 = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
switch_pin_2 = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if switch_pin_1.value():
        led_pin.value(1)
    elif switch_pin_2.value():
        led_pin.value(0)
    time.sleep(0.1)

