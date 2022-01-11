# ******************************************************************************************
# FileName     : 02._oled_button_print
# Description  : 버튼을 누르면 oled 모듈에 누른 버튼 색상 출력
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     :
# ******************************************************************************************


# import
from machine import Pin
from ETboard.lib.OLED_U8G2 import *


# global variable
oled = oled_u8g2()

PinD6 = Pin(D6)                       # 빨강 버튼 핀 지정
PinD7 = Pin(D7)                       # 파랑 버튼 핀 지정
PinD8 = Pin(D8)                       # 초록 버튼 핀 지정
PinD9 = Pin(D9)                       # 노랑 버튼 핀 지정


# setup
def setup():
    PinD6.init(Pin.IN)                # D6을 버튼 입력모드 설정하기
    PinD7.init(Pin.IN)                # D7을 버튼 입력모드 설정하기
    PinD8.init(Pin.IN)                # D8을 버튼 입력모드 설정하기
    PinD9.init(Pin.IN)                # D9을 버튼 입력모드 설정하기


# main loop
def loop():
    button_red = PinD6.value()
    button_blue = PinD7.value()
    button_green = PinD8.value()
    button_yellow = PinD9.value()
    
    oled.clear()
    oled.setLine(2, "PushButton!")    # 처음 OLED 화면 초기화
    
    if button_red == 0:               # 버튼이 눌렸는지 체크 버튼이 눌리면 0 눌리지 않으면 1
        oled.clear()
        oled.setLine(2, "red")        # 2번째 줄에 red 출력하기
        
    if button_blue == 0:
        oled.clear()
        oled.setLine(2, "blue")       # 2번째 줄에 blue 출력하기
        
    if button_green == 0:
        oled.clear()
        oled.setLine(2, "green")      # 2번째 줄에 green 출력하기
        
    if button_yellow == 0:
        oled.clear()
        oled.setLine(2, "yellow")     # 2번째 줄에 yellow 출력하기
    
    oled.display()                    # 저장된 내용을 oled에 보여줌


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
