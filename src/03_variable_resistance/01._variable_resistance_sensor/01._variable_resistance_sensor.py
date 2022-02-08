# ******************************************************************************************
# FileName     : 01._variable_resistance_sensor
# Description  : 가변저항 값 출력 해보기
# Author       : 이승찬
# Created Date : 2021.08.19
# Reference    :
# Modified     : 2022.02.07 : SJI : 헤더 수정
# ******************************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# global variable
sensor = ADC(Pin(A0))                 # 가변저항 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)       # 가변저항 입력 모드 설정


# main loop
def loop():
    sensor_result = sensor.read()     # 가변저항 센서 값 저장
    print(sensor_result)              # 가변저항 센서 값 출력
    
    time.sleep(0.1)                   # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
