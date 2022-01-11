# ******************************************************************************************
# FileName     : 03._oled_photoresistor_sensor_result
# Description  : 조도센서의 값을 읽어서 낮인지 밤인지 판별하는 예제
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     :
# ******************************************************************************************


# import
from machine import Pin, ADC
from ETboard.lib.OLED_U8G2 import *


# global variable
oled = oled_u8g2()
sensor = ADC(Pin(A1))                      # 조도센서 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)            # 조도센서


# main loop
def loop():
    CDS_Value = sensor.read()              # 조도센서 값 받기

    if CDS_Value > 700:
        oled.clear()                       # oled 내용을 지우기
        oled.setLine(2, "Morning !")       # 2번째 줄에 Morning ! 출력하기

    if CDS_Value < 700:  
        oled.clear()                       # oled 내용을 지우기
        oled.setLine(2, "Night !")         # 2번째 줄에 Night ! 출력하기

    oled.display()                         # 저장된 내용을 oled에 보여줌


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
