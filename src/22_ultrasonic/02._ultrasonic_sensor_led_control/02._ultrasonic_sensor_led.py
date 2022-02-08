# ******************************************************************************************
# FileName     : 02._ultrasonic_sensor_led
# Description  : 초음파 센서를 이용하여 거리에 따라 LED 켜보기
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 소스 크린징
# ******************************************************************************************


# import
import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *


# global variable
trigPin = Pin(D9)                                   # 초음파 송신부
echoPin = Pin(D8)                                   # 초음파 수신부

led_red = Pin(D2)                                   # 빨강 LED 핀 지정
led_green = Pin(D4)                                 # 초록 LED 핀 지정
led_yellow = Pin(D5)                                # 노랑 LED 핀 지정


# setup
def setup():
    trigPin.init(Pin.OUT)                           # 초음파 송신부 출력 모드 설정하기
    echoPin.init(Pin.IN)                            # 초음파 수신부 입력 모드 설정하기

    led_red.init(Pin.OUT)                           # 빨강 LED 출력 모드 설정하기
    led_green.init(Pin.OUT)                         # 초록 LED 출력 모드 설정하기
    led_yellow.init(Pin.OUT)                        # 노랑 LED 출력 모드 설정하기


# main loop
def loop():
    # 초음파 송신 후 수신부는 HIGH 상태로 대기
    trigPin.value(LOW)
    echoPin.value(LOW)
    time.sleep_ms(2)
    trigPin.value(HIGH)
    time.sleep_ms(10)
    trigPin.value(LOW)

    duration = time_pulse_us(echoPin, HIGH)         # echoPin 이 HIGH 를 유지한 시간 저장
    distance = ((17 * duration) / 1000)             # 거리 계산

    # 초음파센서 값을 출력
    print(distance, " cm ")                         # 거리를 화면에 출력해줌
    time.sleep_ms(100)                              # 0.1초 대기
    
    # 초음파센서 값에 따라 LED 제어
    if distance < 10:                               # 거리가 10cm 미만이면
        led_red.value(HIGH)                         # 빨강색 LED 켜짐
    else:
        led_red.value(LOW)                          # 빨강색 LED 꺼짐

    if (distance < 20) and (distance >= 10):        # 10cm 이상  20cm 미만이면
        led_yellow.value(HIGH)                      # 노랑색 LED 켜짐
    else:
        led_yellow.value(LOW)                       # 노랑색 LED 꺼짐
        
    if distance >= 20:                              # 20cm 이상이면
        led_green.value(HIGH)                       # 초록색 LED 켜짐
    else:
        led_green.value(LOW)                        # 초록색 LED 꺼짐


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
