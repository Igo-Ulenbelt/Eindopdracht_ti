from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)

def pulse(pin, duration):
    pin.on()
    time.sleep(duration)
    pin.off()
    time.sleep(duration)
    pin.on

def morse(pin, dot_length, text):
    for char in text:
        char = char.upper()
        if char == '.':
            pulse(pin, dot_length)
        elif char == '-':
            pulse(pin, 3 * dot_length)
        elif char == ' ':
            time.sleep(4 * dot_length)

morse(gpio_pin, 0.2, ".--. -.-- - .... --- -.")



