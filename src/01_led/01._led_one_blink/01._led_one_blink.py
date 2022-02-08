# ******************************************************************************************
# FileName     : 01._led_one_blink
# Description  : 빨강 LED 가 켜졌다 꺼졌다 반복
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
led_red = Pin(D2)           # 빨강 LED 핀 지정


# setup
def setup():
    led_red.init(Pin.OUT)   # D2를 LED 출력모드 설정


# main loop
def loop():
    led_red.value(HIGH)     # 빨강 LED 켜기
    time.sleep(1)           # 1초 기다리기

    led_red.value(LOW)      # 빨강 LED 끄기
    time.sleep(1)           # 1초 기다리기

    led_red.value(HIGH)     # 빨강 LED 켜기
    time.sleep(1)           # 1초 기다리기

    led_red.value(LOW)      # 빨강 LED 끄기
    time.sleep(1)           # 1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
