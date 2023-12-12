from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, short_time, long_time):
    pin.on()
    time.sleep(short_time)
    pin.off()
    time.sleep(long_time)
    pin.on

while True:
    pulse(gpio_pin, 0.2, 1.5)

