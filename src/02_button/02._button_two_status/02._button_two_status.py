# ******************************************************************************************
# FileName     : 02._button_two_status
# Description  : 버튼 두 개를 눌렀다 뗐다 해보기
# Author       : 이승찬
# Created Date : 2021.08.19
# Reference    :
# Modified     : 2022.02.07 : SJI : 헤더 수정, 소스 크린징
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
button_red = Pin(D6)                           # 빨강 버튼 핀 지정
button_blue = Pin(D7)                          # 파랑 버튼 핀 지정


# setup
def setup():
    button_red.init(Pin.IN)                    # 빨강 버튼 입력모드 설정하기
    button_blue.init(Pin.IN)                   # 파랑 버튼 입력모드 설정하기


# main loop
def loop():
    button_red_status = button_red.value()     # 빨강 버튼의 값을 저장
    button_blue_status = button_blue.value()   # 파랑 버튼의 값을 저장
    
    if button_red_status == LOW:               # 빨강 버튼이 눌렸는지 체크
        print("빨강 버튼이 눌림")
        
    if button_blue_status == LOW:              # 파랑 버튼이 눌렸는지 체크
        print("파랑 버튼이 눌림") 

    time.sleep(0.1)                            # 0.1초 대기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
