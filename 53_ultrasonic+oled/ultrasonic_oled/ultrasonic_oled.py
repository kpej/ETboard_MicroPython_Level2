# ******************************************************************************************
# FileName     : ultrasonic_oled
# Description  : 초음파센서로 거리를 측정하고 거리에 따라 OLED에 문자열 출력하는 예제
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin, time_pulse_us
from ETboard.lib.OLED_U8G2 import *


# global variable
oled = oled_u8g2()
trigPin = Pin(D9)                                  # 초음파 송신부
echoPin = Pin(D8)                                  # 초음파 수신 부


# setup
def setup():
    trigPin.init(Pin.OUT)                          # 초음파 송신부
    echoPin.init(Pin.IN)                           # 초음파 수신부


# main loop
def loop():
    # 초음파 송신 후 수신부는 HIGH 상태로 대기
    trigPin.value(LOW)
    echoPin.value(LOW)
    time.sleep_ms(2)
    trigPin.value(HIGH)
    time.sleep_ms(10)
    trigPin.value(LOW)
    
    # echoPin 이 HIGH를 유지한 시간 저장
    duration = time_pulse_us(echoPin, HIGH)
    # HIGH 였을 때 시간(초음파 송수신 시간)을 기준으로 거리를 계산
    distance = ((17 * duration) / 1000)
    
    # 초음파센서 값에 따라 OLED 제어
    if distance > 0:                               # 거리가 10cm 미만이면
        oled.clear()
        oled.setLine(2, "danger !")       

    if distance > 20:                              # 10cm 초과이면 20cm 미만이면
        oled.clear()
        oled.setLine(2, "warning !")       
        
    if distance > 30:                              # 20cm 이상이면
        oled.clear()
        oled.setLine(2, "safe !")
        
    oled.display()                                 # 저장된 내용을 oled에 보여줌


if __name__ == "__main__":
    setup()
    while True:
        loop()
        
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
