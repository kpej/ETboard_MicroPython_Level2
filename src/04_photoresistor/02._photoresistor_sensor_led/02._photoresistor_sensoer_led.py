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
led_red = Pin(D2)                     # 빨강 LED 핀 지정
led_blue = Pin(D3)                    # 파랑 LED 핀 지정
led_green = Pin(D4)                   # 초록 LED 핀 지정
led_yellow = Pin(D5)                  # 노랑 LED 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)       # 조도 센서
    led_red.init(Pin.OUT)             # 빨강 LED 출력모드 설정
    led_blue.init(Pin.OUT)            # 파랑 LED 출력모드 설정
    led_green.init(Pin.OUT)           # 초록 LED 출력모드 설정
    led_yellow.init(Pin.OUT)          # 노랑 LED 출력모드 설정


# main loop
def loop():
    sensor_result = sensor.read()     # 조도 센서 값 저장

    # LED를 초기화
    led_red.value(LOW)
    led_blue.value(LOW)
    led_green.value(LOW)
    led_yellow.value(LOW)
    
    if sensor_result < 2000:          # 조도센서 값이 2000이하이면 빨강 LED 킴
        led_red.value(HIGH)
        
    if sensor_result < 1500:          # 조도센서 값이 1500이하이면 파랑 LED 킴
        led_blue.value(HIGH)
        
    if sensor_result < 1000:          # 조도센서 값이 1000이하이면 초록 LED 킴
        led_green.value(HIGH)
        
    if sensor_result < 500:           # 조도센서 값이 500이하이면 노랑 LED 킴
        led_yellow.value(HIGH)


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
