from machine import Pin
from time import sleep

buzzer = Pin(14, Pin.OUT)
buzzer.value(0)
led = Pin(2, Pin.OUT)

for i in range(5):
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)
    if i == 4:
        for _ in range(2):
            led.value(1)
            sleep(0.2)
            led.value(0)
            sleep(0.2)
        



buzzer.value(1)
sleep(0.05)
buzzer.value(0)