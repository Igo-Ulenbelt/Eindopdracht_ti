from machine import ADC, PWM, Pin
import time

led = Pin(20, Pin.OUT)
adc = ADC(Pin(26))


def pulse(pin, high_time, low_time, adc_value):
    sleep_time = 0.6 - ((adc_value / 65535) * 0.4)

    if adc_value == 65535:
        sleep_time = low_time
    elif adc_value == 0:
        sleep_time = high_time

    pin.on()
    time.sleep(sleep_time)
    pin.off()
    time.sleep(sleep_time)

while True:
    adc_value = adc.read_u16()
    time.sleep(0.01)
    pulse(led, 1, 0.2, adc_value)
