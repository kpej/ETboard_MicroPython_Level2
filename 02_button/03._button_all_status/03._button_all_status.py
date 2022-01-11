# ******************************************************************************************
# FileName     : 03._button_all_status
# Description  : 모든 버튼 상태를 쉘에 출력
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
PinD6 = Pin(D6)                            # 빨강 버튼 핀 지정
PinD7 = Pin(D7)                            # 파랑 버튼 핀 지정
PinD8 = Pin(D8)                            # 초록 버튼 핀 지정
PinD9 = Pin(D9)                            # 노랑 버튼 핀 지정


# setup
def setup():
    PinD6.init(Pin.IN)                     # 빨강 버튼 입력모드 설정하기
    PinD7.init(Pin.IN)                     # 파랑 버튼 입력모드 설정하기
    PinD8.init(Pin.IN)                     # 초록 버튼 입력모드 설정하기
    PinD9.init(Pin.IN)                     # 노랑 버튼 입력모드 설정하기


# main loop
def loop():
    button_red_status = PinD6.value()      # 빨강 버튼 입력모드 설정하기
    button_blue_status = PinD7.value()     # 파랑 버튼 입력모드 설정하기
    button_green_status = PinD8.value()    # 초록 버튼 입력모드 설정하기
    button_yellow_status = PinD9.value()   # 노랑 버튼 입력모드 설정하기
    
    if button_red_status == 0:             # 빨간 버튼이 눌렸는지 체크 버튼이 눌리면 0 눌리지 않으면 1
        print("빨강버튼이 눌림")
        
    if button_blue_status == 0:            # 파랑 버튼이 눌렸는지 체크 버튼이 눌리면 0 눌리지 않으면 1
        print("파랑버튼이 눌림")
        
    if button_green_status == 0:           # 초록 버튼이 눌렸는지 체크 버튼이 눌리면 0 눌리지 않으면 1
        print("초록버튼이 눌림")
        
    if button_yellow_status == 0:          # 노랑 버튼이 눌렸는지 체크 버튼이 눌리면 0 눌리지 않으면 1
        print("노랑버튼이 눌림") 
    
    print(button_red_status, end=' ')
    print(button_blue_status, end=' ')
    print(button_green_status, end=' ')
    print(button_yellow_status)
    
    time.sleep(0.1)                        # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
