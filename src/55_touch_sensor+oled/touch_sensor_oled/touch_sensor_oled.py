# ******************************************************************************************
# FileName     : touch_sensor_oled
# Description  : 터치센서에 터치시 OLED 에 "touch" 출력
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     :
# ******************************************************************************************


# import
from machine import Pin
from ETboard.lib.OLED_U8G2 import *


# global definition
oled = oled_u8g2()

pt = Pin(D2)                               # 터치센서 핀 지정


# setup
def setup():
    pt.init(Pin.IN)                        # 터치센서 입력모드 설정


# main loop
def loop():
    oled.clear()                           # OLED 스크린 모두 지우기
    oled.setLine(2, " ")
    
    if pt.value() == 1:
        oled.clear()
        oled.setLine(2, "touch")           # OLED 2번째 라인에 touch 설정
        
    oled.display()                         # OLED에 출력 하기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
