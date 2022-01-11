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
PinD2 = Pin(D2)            # 빨강 LED 핀 지정
PinD3 = Pin(D3)            # 파랑 LED 핀 지정
PinD4 = Pin(D4)            # 초록 LED 핀 지정
PinD5 = Pin(D5)            # 노랑 LED 핀 지정


# setup
def setup():
    PinD2.init(Pin.OUT)    # 빨강 LED 출력모드 설정
    PinD3.init(Pin.OUT)    # 파랑 LED 출력모드 설정
    PinD4.init(Pin.OUT)    # 초록 LED 출력모드 설정
    PinD5.init(Pin.OUT)    # 노랑 LED 출력모드 설정


# main loop
def loop():
    PinD2.value(HIGH)      # 빨강 LED 켜기
    time.sleep(1)          # 1초 기다리기
    
    PinD3.value(HIGH)      # 파랑 LED 켜기
    time.sleep(1)          # 1초 기다리기
    
    PinD5.value(HIGH)      # 노랑 LED 켜기
    time.sleep(1)          # 1초 기다리기
    
    PinD4.value(HIGH)      # 초록 LED 켜기
    time.sleep(1)          # 1초 기다리기
    
    PinD2.value(LOW)       # 빨강 LED 끄기
    PinD3.value(LOW)       # 파랑 LED 끄기
    PinD4.value(LOW)       # 초록 LED 끄기
    PinD5.value(LOW)       # 노랑 LED 끄기
    time.sleep(1)          # 1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
