# ******************************************************************************************
# FileName     : 03._temperature_sensor_temp_led
# Description  : 온도 센서값을 받고 값을 온도값 마다 다른 LED 켜기
# Author       : 이승찬
# Created Date : 2021.08.17
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
import math
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# global variable
R1 = 10000
c1 = 1.009249522e-03
c2 = 2.378405444e-04
c3 = 2.019202697e-07

sensor = ADC(Pin(A2))                                    # 온도센서 핀 지정

PinD2 = Pin(D2)                                          # 빨강 LED 핀 지정
PinD3 = Pin(D3)                                          # 파랑 LED 핀 지정
PinD4 = Pin(D4)                                          # 초록 LED 핀 지정
PinD5 = Pin(D5)                                          # 노랑 LED 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)                          # 온도센서 입력모드 설정

    PinD2.init(Pin.OUT)                                  # D2를 빨간 LED 출력모드 설정
    PinD3.init(Pin.OUT)                                  # D3를 파란 LED 출력모드 설정
    PinD4.inti(Pin.OUT)                                  # D4를 초록 LED 출력모드 설정
    PinD5.init(Pin.OUT)                                  # D5를 노랑 LED 출력모드 설정


# main loop
def loop():
    Vo = sensor.read()                                   # 가변저항 센서 값 저장

    # 온도 센서 값을 이용하여 실제 온도 값 으로 변환
    R2 = R1 * (4095.0 / Vo - 1.0)
    logR2 = math.log(R2)
    T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2))
    Tc = T - 273.15
    
    if Tc <= 10:                                         # 온도가 10도 이하면 파랑 LED 켜기
        PinD2.value(LOW)
        PinD3.value(HIGH)
        PinD4.value(LOW) 
        PinD5.value(LOW) 
        print("파랑온")

    if Tc >= 10 && Tc < 20:                                          # 온도가 10도 이상 20도 미만이면 초록 LED 켜기
        PinD2.value(LOW)
        PinD3.value(LOW)
        PinD4.value(HIGH) 
        PinD5.value(LOW) 
        print("초록온")

    if Tc >= 20 && Tc < 30:                                          # 온도가 20도이상 30도 미만이면 노랑 LED 켜기
        PinD2.value(LOW)
        PinD3.value(LOW)
        PinD4.value(LOW) 
        PinD5.value(HIGH) 
        print("노랑온")

    if Tc >= 30:                                         # 온도가 30도 이상이면 빨강 LED 켜기
        PinD2.value(HIGH)
        PinD3.value(LOW)
        PinD4.value(LOW) 
        PinD5.value(LOW) 
        print("빨강온")

    time.sleep(0.2)                                      # 0.2초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
