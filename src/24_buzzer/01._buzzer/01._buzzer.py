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
buzzer = Pin(D2)                    # 부저 핀 지정


# setup
def setup():
    buzzer.init(Pin.OUT)            # 부저 출력모드 설정하기


# main loop
def loop():
    # 부저 소리내기
    buzzer.value(HIGH)
    time.sleep(0.001)        
    buzzer.value(LOW)
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
