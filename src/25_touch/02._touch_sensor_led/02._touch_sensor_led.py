# ******************************************************************************************
# FileName     : 02._touch_sensor_led
# Description  : 터치센서에 터치가 되면 LED를 켜는 예제
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
pt = Pin(D2)                   # 터치센서 핀 지정

led_blue = Pin(D3)             # 파랑 LED 핀 지정
led_green = Pin(D4)            # 초록 LED 핀 지정
led_yellow = Pin(D5)           # 노랑 LED 핀 지정


# setup
def setup():
    pt.init(Pin.IN)            # 터치센서 입력모드 설정

    led_blue.init(Pin.OUT)     # D3를 LED 출력모드 설정
    led_green.init(Pin.OUT)    # D4를 LED 출력모드 설정
    led_yellow.init(Pin.OUT)   # D5를 LED 출력모드 설정


# main loop
def loop():
    led_blue.value(LOW)        # 파랑 LED 끄기
    led_green.value(LOW)       # 초록 LED 끄기
    led_yellow.value(LOW)      # 노랑 LED 끄기
    
    if pt.value() == 1:
        led_blue.value(HIGH)   # 파랑 LED 켜기
        led_green.value(HIGH)  # 초록 LED 켜기
        led_yellow.value(HIGH) # 노랑 LED 켜기
        
    time.sleep(0.1)            # 0.1초 대기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
