# ******************************************************************************************
# FileName     : 01._ultrasonic_sensor
# Description  : 초음파센서를 사용하는 기본적인 예제
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *


# global variable
trigPin = Pin(D9)                                  # 초음파 송신부
echoPin = Pin(D8)                                  # 초음파 수신부


# setup
def setup():
    trigPin.init(Pin.OUT)                          # 초음파 송신부 출력 모드 설정하기
    echoPin.init(Pin.IN)                           # 초음파 수신부 입력 모드 설정하기


# main loop
def loop():
    # 초음파 송신 후 수신부는 HIGH 상태로 대기
    trigPin.value(LOW)
    echoPin.value(LOW)
    time.sleep_ms(2)
    trigPin.value(HIGH)
    time.sleep_ms(10)
    trigPin.value(LOW)
    
    # echoPin 이 HIGH 를 유지한 시간 저장
    duration = time_pulse_us(echoPin, HIGH)
    # HIGH 였을 때 시간(초음파 송수신 시간)을 기준으로 거리를 계산
    distance = 17 * duration / 1000
    
    # 초음파센서 값을 출력
    print(distance, " cm ")                        # 거리를 화면에 출력해줌
    time.sleep(0.1)                                # 0.1초 대기


if __name__ == "__main__":
    setup()
    while True:
        loop()
        
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
