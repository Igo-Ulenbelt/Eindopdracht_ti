from machine import Pin
import time

servo_pin = Pin(20, Pin.OUT)

def pulse(pin, high_time, low_time):
    pin.on()
    time.sleep(high_time)
    pin.off()
    time.sleep(low_time)

def servo_pulse(position):
    pulse(servo_pin, 0.0005 + 0.002 * position / 100, 0.02)

while True:
    for i in range(0, 101):
        servo_pulse(i)
    for i in range(100, -1, -1):
        servo_pulse(i)


