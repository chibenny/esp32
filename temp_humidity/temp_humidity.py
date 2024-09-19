from time import sleep

import dht
from lcd_i2c import LCD
from machine import Pin, SoftI2C

sensor_data = dht.DHT11(Pin(15))
button = Pin(2, Pin.IN)

I2C_ADDR = 0x27
NUM_ROWS = 2
NUM_COLS = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS)

lcd.begin()
lcd.print("Hello, World!")
lcd.clear()


def get_room_data():
    sensor_data.measure()

    t = (sensor_data.temperature() * 1.8) + 32
    h = sensor_data.humidity()

    temp = f"Temp: {t}F"
    hum = f"Humidity {h}%"

    lcd.home()
    lcd.print(temp)
    lcd.set_cursor(col=0, row=1)
    lcd.print(hum)


while True:
    get_room_data()
    sleep(5)
    lcd.clear()
    lcd.home()
    lcd.print("Refreshing...")
    sleep(0.7)
    lcd.clear()
