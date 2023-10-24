import time
from machine import Pin
from ETboard.lib.pin_define import *

import sys
import time
from ETboard_BluetoothSerial import BluetoothSerial

# global variable
led_red = Pin(D2)           # 빨강 LED 핀 지정
SerialBT = BluetoothSerial()       # bluetooth

def handle_data(v):
    print("입력값 = ", v)
    str_v = chr(v[0])
    if (str_v == '1'):
        print('빨강 온 !!!!')
        led_red.value(HIGH)     # 빨강 LED 켜기
    elif (str_v == '2'):
        print('빨강 오프 !!!!')
        led_red.value(LOW)     # 빨강 LED 켜기        
        
# setup
def setup():
    led_red.init(Pin.OUT)   # D2를 LED 출력모
    SerialBT.on_received(handle_data)
    
    
# main loop
def loop():
    pass


if __name__ == "__main__":
    setup()
    while True:
        loop()

