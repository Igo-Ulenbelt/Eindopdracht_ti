import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

colors = [
    [255, 0, 0],   # Rood
    [0, 255, 0],   # Groen
    [0, 0, 255]    # Blauw
]

while True:
    for color in colors:
        for i in range(len(np)):
            np[i] = color
            np.write()
            time.sleep(0.5)