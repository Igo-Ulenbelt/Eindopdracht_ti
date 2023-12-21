import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

value = 0

while True:
    for i in range(len(np)):
        np[i] = [255, 0, 0]
        np.write()
        time.sleep(0.5)

    for i in range(len(np)):
        np[i] = (0, 0, 0)

    np.write()
    time.sleep(0.5)
