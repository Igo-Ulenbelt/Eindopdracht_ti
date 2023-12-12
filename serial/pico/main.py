import machine
from machine import Pin
import time

# Use on-board led
led = Pin(25, Pin.OUT)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

# Blink led to confirm successful flashing
for _ in range(5):
    led(0)
    time.sleep(.1)
    led(1)
    time.sleep(.1)

# Wait for data from the connection
while True:
    data = input()

    print("Received '" + data + "'.")
    if data == '0':
        led(0)
        print("Turning led off.")
    elif data == '1':
        led(1)
        print("Turning led on.")
    elif data == '2':
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = 27 - (reading - 0.706) / 0.001721
        print(f"Temperature: {temperature} °C")
    else:
        print("Unknown command.")