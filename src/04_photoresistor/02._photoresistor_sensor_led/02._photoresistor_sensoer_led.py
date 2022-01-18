# ******************************************************************************************
# FileName     : 02._photoresistor_sensoer_led
# Description  : 조도센서 값에 따라 순차적으로 LED 가 켜짐
#                빨강 - 파랑 - 초록 - 노랑 순서
# Author       : 이승찬
# Created Date : 2021.08.13
# Reference    :
# Modified     :
# ******************************************************************************************


# import
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# global variable
sensor = ADC(Pin(A1))                 # 조도센서 핀 지정
PinD2 = Pin(D2)                       # 빨강 LED 핀 지정
PinD3 = Pin(D3)                       # 파랑 LED 핀 지정
PinD4 = Pin(D4)                       # 초록 LED 핀 지정
PinD5 = Pin(D5)                       # 노랑 LED 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)       # 조도 센서
    PinD2.init(Pin.OUT)               # 빨강 LED 출력모드 설정
    PinD3.init(Pin.OUT)               # 파랑 LED 출력모드 설정
    PinD4.init(Pin.OUT)               # 초록 LED 출력모드 설정
    PinD5.init(Pin.OUT)               # 노랑 LED 출력모드 설정


# main loop
def loop():
    sensor_result = sensor.read()     # 조도 센서 값 저장

    # LED를 초기화
    PinD2.value(LOW)
    PinD3.value(LOW)
    PinD4.value(LOW)
    PinD5.value(LOW)
    
    if sensor_result < 2000:          # 조도센서 값이 2000이하이면 빨강 LED 킴
        PinD2.value(HIGH)
        
    if sensor_result < 1500:          # 조도센서 값이 1500이하이면 파랑 LED 킴
        PinD3.value(HIGH)
        
    if sensor_result < 1000:          # 조도센서 값이 1000이하이면 초록 LED 킴
        PinD4.value(HIGH)
        
    if sensor_result < 500:           # 조도센서 값이 500이하이면 노랑 LED 킴
        PinD5.value(HIGH)


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
