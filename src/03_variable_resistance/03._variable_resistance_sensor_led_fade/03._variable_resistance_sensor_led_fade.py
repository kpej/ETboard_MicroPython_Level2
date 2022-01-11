# ******************************************************************************************
# FileName     : 03._variable_resistance_sensor_led_fade
# Description  : 가변저항 값에 따라 빨강 LED 의 밝기가 달라짐
#                가변저항 값을 쉘에 출력
# Author       : 이승찬
# Created Date : 2021.08.13
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import ADC, Pin, PWM
from ETboard.lib.pin_define import *


# global variable
sensor = ADC(Pin(A0))                     # 가변저항 핀 지정
PinD2 = Pin(D2)                           # 빨강 LED 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)           # 가변저항 입력 모드 설정
    PinD2.init(Pin.OUT)                   # 빨강 LED 출력 모드 설정


# main loop
def loop():
    sensor_result = sensor.read() / 3     # 가변저항 센서 값 저장
    print(sensor_result)

    # 가변저항값을 이용하여 빨강 LED의 밝기를 조절
    pwm2 = PWM(Pin(D2), 500, int(sensor_result))

    time.sleep(0.1)                       # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
