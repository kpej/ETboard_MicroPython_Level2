# ******************************************************************************************
# FileName     : 02._led_two_blink
# Description  : LED 두개를 켰다 껐다 해보기
# Author       : 이승찬
# Created Date : 2021.08.13
# Reference    :
# Modified     : 2022.02.07 : SJI : 헤더 수정
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
led_red = Pin(D2)             # 빨강 LED 핀 지정
led_yellow = Pin(D5)          # 노랑 LED 핀 지정


# setup
def setup():
    led_red.init(Pin.OUT)     # 빨강 LED 출력모드 설정
    led_yellow.init(Pin.OUT)  # 노랑 LED 출력모드 설정


# main loop
def loop():
    led_red.value(HIGH)       # 빨강 LED 켜기
    led_yellow.value(HIGH)    # 노랑 LED 켜기
    time.sleep(2)             # 2초 기다리기
    
    led_red.value(LOW)        # 빨강 LED 끄기
    led_yellow.value(LOW)     # 노랑 LED 끄기
    time.sleep(2)             # 2초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
