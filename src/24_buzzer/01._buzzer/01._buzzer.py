# ******************************************************************************************
# FileName     : 01._buzzer
# Description  : 부저를 이용하여 소리 내보기
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 주석 수정, 소스 크린징
# Modified     : 2022.02.15 : SJI : 주석 수정, 소스 크린징
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
buzzer = Pin(D6)                    # 부저 핀 지정

# setup
def setup():
    buzzer.init(Pin.OUT)            # 부저 출력모드 설정하기

# main loop
def loop():                         
    for i in range(80) :             # 소리를 짧게 한번 냄
        buzzer.value(HIGH)
        time.sleep(0.001)
        buzzer.value(LOW)
        time.sleep(0.001)
    time.sleep(1)

if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
