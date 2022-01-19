# ******************************************************************************************
# FileName     : 02._variable_resistance_sensor_led
# Description  : 가변저항 값에 따라 LED 가 순차적으로 켜짐(빨강-파랑-노랑-초록)
# Author       : 이인정
# Created Date : 2021.05.31
# Reference    :
# Modified     : 2021.06.01 : LIJ : 헤더수정
# ******************************************************************************************


# import
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# global variable
sensor = ADC(Pin(A0))                    # 가변저항 핀 지정

led_red = Pin(D2)                        # 빨강 LED 핀 지정
led_blue = Pin(D3)                       # 파랑 LED 핀 지정
led_green = Pin(D4)                      # 초록 LED 핀 지정
button_yellow = Pin(D5)                  # 노랑 LED 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)          # 가변저항 입력 모드 설정

    led_red.init(Pin.OUT)                # 빨강 LED 출력모드 설정
    led_blue.init(Pin.OUT)               # 파랑 LED 출력모드 설정
    led_green.init(Pin.OUT)              # 초록 LED 출력모드 설정
    button_yellow.init(Pin.OUT)          # 노랑 LED 출력모드 설정


# main loop
def loop():
    sensor_result = sensor.read()        # 가변저항 센서 값 저장

    # LED 전부 초기화
    led_red.value(LOW)
    led_blue.value(LOW)
    led_green.value(LOW)
    button_yellow.value(LOW)
    
    if sensor_result > 500:              # 가변저항 값이 500 초과이면 빨강 LED 켜기
        led_red.value(HIGH)
        
    if sensor_result > 1000:             # 가변저항 값이 1000 초과이면 파랑 LED 켜기
        led_blue.value(HIGH)
        
    if sensor_result > 1500:             # 가변저항 값이 1500 초과이면 노랑 LED 켜기
        button_yellow.value(HIGH)
        
    if sensor_result > 2000:             # 가변저항 값이 2000 초과이면 초록 LED 켜기
        led_green.value(HIGH)


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
