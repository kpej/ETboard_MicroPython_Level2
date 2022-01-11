# ******************************************************************************************
# FileName     : 01._buzzer
# Description  : 부저를 이용하여 소리를 내는 예제
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
PinD2 = Pin(D2)                    # 부저 핀 지정


# setup
def setup():
    PinD2.init(Pin.OUT)            # 부저 출력모드 설정하기


# main loop
def loop():
    # 부저 소리내기
    PinD2.value(HIGH)
    time.sleep(0.001)        
    PinD2.value(LOW)      
    time.sleep(0.001)         


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
