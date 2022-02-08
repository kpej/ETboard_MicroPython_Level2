# ******************************************************************************************
# FileName     : 04._led_order_blink
# Description  : LED 4개를 순차적으로 on 시킴
# Author       : 이승찬
# Created Date : 2021.08.19
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
led_red = Pin(D2)            # 빨강 LED 핀 지정
led_blue = Pin(D3)           # 파랑 LED 핀 지정
led_green = Pin(D4)          # 초록 LED 핀 지정
led_yellow = Pin(D5)         # 노랑 LED 핀 지정


# setup
def setup():
    led_red.init(Pin.OUT)    # 빨강 LED 출력모드 설정
    led_blue.init(Pin.OUT)   # 파랑 LED 출력모드 설정
    led_green.init(Pin.OUT)  # 초록 LED 출력모드 설정
    led_yellow.init(Pin.OUT) # 노랑 LED 출력모드 설정


# main loop
def loop():
    led_red.value(HIGH)      # 빨강 LED 켜기
    time.sleep(1)            # 1초 기다리기
    
    led_blue.value(HIGH)     # 파랑 LED 켜기
    time.sleep(1)            # 1초 기다리기
    
    led_yellow.value(HIGH)   # 노랑 LED 켜기
    time.sleep(1)            # 1초 기다리기
    
    led_green.value(HIGH)    # 초록 LED 켜기
    time.sleep(1)            # 1초 기다리기
    
    led_red.value(LOW)       # 빨강 LED 끄기
    led_blue.value(LOW)      # 파랑 LED 끄기
    led_green.value(LOW)     # 초록 LED 끄기
    led_yellow.value(LOW)    # 노랑 LED 끄기
    time.sleep(1)            # 1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
