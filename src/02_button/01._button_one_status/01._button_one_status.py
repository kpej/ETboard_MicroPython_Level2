# ******************************************************************************************
# FileName     : 01._button_one_status
# Description  : 버튼 한 개를 눌렀다 뗐다 해보기
#                시리얼 모니터로 출력
# Author       : 이승찬
# Created Date : 2021.08.19
# Reference    :
# Modified     : 2022.02.07 : SJI : 헤더 수정, 소스 크린징
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global function
button_red = Pin(D6)                                  # 빨강 버튼 핀 지정


# setup
def setup():
    button_red.init(Pin.IN)                           # 빨강 버튼 입력모드 설정하기


# main loop
def loop():
    button_red_status = button_red.value()            # 빨강 버튼의 값을 저장
    
    if button_red_status == LOW:                      # 빨강 버튼 상태 체크
        print("버튼이 눌림")
    else:
        print("버튼이 눌리지 않음")
        
    time.sleep(0.1)                                   # 0.1초 대기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
