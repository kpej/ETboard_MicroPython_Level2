# ******************************************************************************************
# FileName     : 04._led_button_control
# Description  : 버튼을 눌러 같은 색의 LED를 켜보기
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     : 2022.02.07 : SJI : 헤더 수정
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
led_red = Pin(D2)                             # 빨강 LED 핀 지정
led_blue = Pin(D3)                            # 파랑 LED 핀 지정
led_green = Pin(D4)                           # 초록 LED 핀 지정
led_yellow = Pin(D5)                          # 노랑 LED 핀 지정

button_red = Pin(D6)                          # 빨강 버튼 핀 지정
button_blue = Pin(D7)                         # 파랑 버튼 핀 지정
button_green = Pin(D8)                        # 초록 버튼 핀 지정
button_yellow = Pin(D9)                       # 노랑 버튼 핀 지정

button_red_value = 0                          # 빨강 버튼의 상태
button_red_old_value = 1                      # 빨강 버튼의 이전 상태
led_red_status = 0                            # 빨강 LED 상태

button_blue_value = 0                         # 파랑 버튼의 상태
button_blue_old_value = 1                     # 파랑 버튼의 이전 상태
led_blue_status = 0                           # 파랑 LED 상태

button_green_value = 0                        # 초록 버튼의 상태
button_green_old_value = 1                    # 초록 버튼의 이전 상태
led_green_status = 0                          # 초록 LED 상태

button_yellow_value = 0                       # 노랑 버튼의 상태
button_yellow_old_value = 1                   # 노랑 버튼의 이전 상태
led_yellow_status = 0                         # 노랑 LED 상태


# setup
def setup():
    led_red.init(Pin.OUT)                     # 빨강 LED 출력모드 설정하기
    led_blue.init(Pin.OUT)                    # 파랑 LED 출력모드 설정하기
    led_green.init(Pin.OUT)                   # 초록 LED 출력모드 설정하기
    led_yellow.init(Pin.OUT)                  # 노랑 LED 출력모드 설정하기

    button_red.init(Pin.IN)                   # 빨강 버튼 입력모드 설정하기
    button_blue.init(Pin.IN)                  # 파랑 버튼 입력모드 설정하기
    button_green.init(Pin.IN)                 # 초록 버튼 입력모드 설정하기
    button_yellow.init(Pin.IN)                # 노랑 버튼 입력모드 설정하기


# mainloop
def loop():
    # 전역변수 불러오기
    global button_red_value, button_red_old_value, led_red_status
    global button_blue_value, button_blue_old_value, led_blue_status
    global button_green_value, button_green_old_value, led_green_status
    global button_yellow_value, button_yellow_old_value, led_yellow_status

    # 각각의 버튼 상태 저장하기
    button_red_value = button_red.value()
    button_blue_value = button_blue.value()
    button_green_value = button_green.value()
    button_yellow_value = button_yellow.value()

    # 빨강 버튼 으로 빨강 LED 제어
    if button_red_value == 0 and button_red_old_value == 1:
        led_red_status = 1 - led_red_status
    button_red_old_value = button_red_value
    if led_red_status == 1:
        led_red.value(HIGH)
    else:
        led_red.value(LOW)

    # 파랑 버튼 으로 파랑 LED 제어
    if button_blue_value == 0 and button_blue_old_value == 1:
        led_blue_status = 1 - led_blue_status
    button_blue_old_value = button_blue_value
    if led_blue_status == 1:
        led_blue.value(HIGH)
    else:
        led_blue.value(LOW)

    # 초록 버튼 으로 초록 LED 제어
    if button_green_value == 0 and button_green_old_value == 1:
        led_green_status = 1 - led_green_status
    button_green_old_value = button_green_value
    if led_green_status == 1:
        led_green.value(HIGH)
    else:
        led_green.value(LOW)

    # 노랑 버튼 으로 노랑 LED 제어
    if button_yellow_value == 0 and button_yellow_old_value == 1:
        led_yellow_status = 1 - led_yellow_status
    button_yellow_old_value = button_yellow_value
    if led_yellow_status == 1:
        led_yellow.value(HIGH)
    else:
        led_yellow.value(LOW)


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
