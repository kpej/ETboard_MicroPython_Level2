# ******************************************************************************************
# FileName     : 02._led_two_blink
# Description  : 빨간 노랑 LED 를 켜고 끄는 예제
# Author       : 이승찬
# Created Date : 2021.08.13
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
PinD2 = Pin(D2)            # 빨강 LED 핀 지정
PinD5 = Pin(D5)            # 노랑 LED 핀 지정


# setup
def setup():
    PinD2.init(Pin.OUT)    # 빨강 LED 출력모드 설정
    PinD5.init(Pin.OUT)    # 노랑 LED 출력모드 설정


# main loop
def loop():
    PinD2.value(HIGH)      # 빨강 LED 켜기
    PinD5.value(HIGH)      # 노랑 LED 켜기
    time.sleep(2)          # 2초 기다리기
    
    PinD2.value(LOW)       # 빨강 LED 끄기
    PinD5.value(LOW)       # 노랑 LED 끄기
    time.sleep(2)          # 2초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
