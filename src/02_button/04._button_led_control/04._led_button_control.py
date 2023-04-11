# ******************************************************************************************
# FileName     : 05._led_button_control_2
# Description  : 빨강 버튼을 눌러 빨강 LED를 켜보기
# Author       : 손정인
# Created Date : 2022.02.07
# Reference    :
# Modified     : 2023.03.28 : PEJ : 파일 순서 수정
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *

# global variable
led_red = Pin(D2)                             # 빨강 LED 핀 지정

button_red = Pin(D6)                          # 빨강 버튼 핀 지정

button_red_value = 0                          # 빨강 버튼의 상태
button_red_old_value = 1                      # 빨강 버튼의 이전 상태
led_red_status = 0                            # 빨강 LED 상태

# setup
def setup():
    led_red.init(Pin.OUT)                     # 빨강 LED 출력모드 설정하기
    
    button_red.init(Pin.IN)                   # 빨강 버튼 입력모드 설정하기

# mainloop
def loop():
    # 전역변수 불러오기
    global button_red_value, button_red_old_value, led_red_status

    # 빨강 버튼 상태 저장하기
    button_red_value = button_red.value()
    
    # 빨강 버튼 으로 빨강 LED 제어
    if button_red_value == 0 and button_red_old_value == 1:
        led_red_status = 1 - led_red_status
    button_red_old_value = button_red_value
    if led_red_status == 1:
        led_red.value(HIGH)
    else:
        led_red.value(LOW)
        
if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
