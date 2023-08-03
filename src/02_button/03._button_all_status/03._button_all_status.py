# ******************************************************************************************
# FileName     : 03._button_all_status
# Description  : 모든 버튼을 눌렀다 뗐다 해보기 
#                쉘에 출력
# Author       : 이승찬
# Created Date : 2021.08.19
# Reference    :
# Modified     : 2022.02.07 : SJI : 헤더 수정, 주석 수정, T소스 크린징
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
button_red = Pin(D6)                                 # 빨강 버튼 핀 지정
button_blue = Pin(D7)                                # 파랑 버튼 핀 지정
button_green = Pin(D8)                               # 초록 버튼 핀 지정
button_yellow = Pin(D9)                              # 노랑 버튼 핀 지정


# setup
def setup():
    button_red.init(Pin.IN)                          # 빨강 버튼 입력모드 설정하기
    button_blue.init(Pin.IN)                         # 파랑 버튼 입력모드 설정하기
    button_green.init(Pin.IN)                        # 초록 버튼 입력모드 설정하기
    button_yellow.init(Pin.IN)                       # 노랑 버튼 입력모드 설정하기


# main loop
def loop():
    button_red_status = button_red.value()           # 빨강 버튼의 값을 저장
    button_blue_status = button_blue.value()         # 파랑 버튼의 값을 저장
    button_green_status = button_green.value()       # 초록 버튼의 값을 저장
    button_yellow_status = button_yellow.value()     # 노랑 버튼의 값을 저장
    
    if button_red_status == LOW:                     # 빨강 버튼 상태 체크 
        print("빨강버튼이 눌림")
        
    if button_blue_status == LOW:                    # 파랑 버튼 상태 체크 
        print("파랑버튼이 눌림")
        
    if button_green_status == LOW:                   # 초록 버튼 상태 체크 
        print("초록버튼이 눌림")
        
    if button_yellow_status == LOW:                  # 노랑 버튼 상태 체크 
        print("노랑버튼이 눌림") 
    
    print(button_red_status, end=' ')
    print(button_blue_status, end=' ')
    print(button_green_status, end=' ')
    print(button_yellow_status)
    
    time.sleep(0.1)                                  # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
