# ******************************************************************************************
# FileName     : 02._ultrasonic_sensor_led
# Description  : 초음파 센서를 이용하여 거리에따라 LED 를 점등하는 예제
#                (20cm 이상 초록색, 10cm 이상 20cm 미만 노랑색, 10cm 미만 빨강색)
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import tim
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *


# global variable
trigPin = Pin(D9)                                   # 초음파 송신부
echoPin = Pin(D8)                                   # 초음파 수신부

Pin2 = Pin(D2)
Pin4 = Pin(D4)
Pin5 = Pin(D5)


# setup
def setup():
    trigPin.init(Pin.OUT)                           # 초음파 송신부 출력 모드 설정하기
    echoPin.init(Pin.IN)                            # 초음파 수신부 입력 모드 설정하기

    PinD2.init(Pin.OUT)                             # 빨강 LED 출력 모드 설정하기
    PinD4.init(Pin.OUT)                             # 초록 LED 출력 모드 설정하기
    PinD5.init(Pin.OUT)                             # 노랑 LED 출력 모드 설정하기


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
    distance = ((17 * duration) / 1000)             # HIGH 였을 때 시간(초음파 송수신 시간)을 기준으로 거리를 계산

    # 초음파센서 값을 출력
    print(distance, " cm ")                         # 거리를 화면에 출력해줌
    time.sleep_ms(100)                              # 0.1초 대기
    
    # 초음파센서 값에 따라 LED 제어
    if distance < 10:                               # 거리가 10cm 미만이면
        PinD2.value(HIGH)                           # 빨강색 LED 켜짐
    else:
        PinD2.value(LOW)                            # 빨강색 LED 꺼짐

    if (distance < 20) and (distance > 10):         # 10cm 초과 그리고 20cm 미만
        PinD5.value(HIGH)                           # 노랑색 LED 켜짐
    else:
        PinD5.value(LOW)                            # 노랑색 LED 꺼짐
        
    if distance > 20:                               # 20cm 이상이면
        PinD4.value(HIGH)                           # 초록색 LED 켜짐
    else:
        PinD4.value(LOW)                            # 초록색 LED 꺼짐


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
