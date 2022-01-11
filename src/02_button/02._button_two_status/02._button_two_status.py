# ******************************************************************************************
# FileName     : 02._button_two_status
# Description  : 빨강, 파랑 버튼 상태를 쉘에 출력 하는 예제
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
PinD6 = Pin(D6)                        # 빨강 버튼 핀 지정
PinD7 = Pin(D7)                        # 파랑 버튼 핀 지정


# setup
def setup():
    PinD6.init(Pin.IN)                 # 빨강 버튼 입력모드 설정하기
    PinD7.init(Pin.IN)                 # 파랑 버튼 입력모드 설정하기


# main loop
def loop():
    button_red_status = PinD6.value()
    button_blue_status = PinD7.value()
    
    if button_red_status == 0:         # 빨강 버튼이 눌렸는지 체크
        print("빨강 버튼이 눌림")
        
    if button_blue_status == 0:        # 파랑 버튼이 눌렸는지 체크
        print("파랑 버튼이 눌림") 

    time.sleep(0.1)                    # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
