# ******************************************************************************************
# FileName     : 01._button_one_status
# Description  : 빨강 버튼 상태를 쉘에 출력 하는 예제
# Author       : 이승찬
# Created Date : 2021.08.19
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global function
PinD6 = Pin(D6)                                  # 빨강 버튼 핀 지정


# setup
def setup():
    PinD6.init(Pin.IN)                           # 빨강 버튼 입력모드 설정하기


# main loop
def loop():
    button_red_status = PinD6.value()            # 빨강 버튼 상태값 변수에 저장
    
    if button_red_status == 0:                   # 빨강 버튼 상태 체크
        print("버튼이 눌림")
    else:
        print("버튼이 눌리지 않음")
        
    time.sleep(0.1)                              # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
