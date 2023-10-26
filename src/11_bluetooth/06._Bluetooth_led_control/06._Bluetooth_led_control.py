# ******************************************************************************************
# FileName     : 06._Bluetooth_led_control
# Description  : 블루투스 통신으로 LED 제어해 보기
# Author       : 손철수
# Created Date : 2023.10.25
# Reference    :
# Modified     : 2023.10.25 : PEJ : 헤더, 푸터 주석 추가, 코드 주석 추가, 파일명 변경
# ******************************************************************************************


import sys
import time
from machine import Pin
from ETboard.lib.pin_define import *
from ETboard.lib.BluetoothSerial import BluetoothSerial


# global variable
led_red = Pin(D2)                                          # 빨강 LED 핀 지정
led_blue = Pin(D3)                                         # 파랑 LED 핀 지정
led_green = Pin(D4)                                        # 초록 LED 핀 지정
led_yellow = Pin(D5)                                       # 노랑 LED 핀 지정

SerialBT = BluetoothSerial()


# 수신 받은 데이터를 처리
def handle_data(msg):
    print("받은 문자열:", msg)                             # 수신받은 데이터를 쉘에 출력
    if (msg == '1'):
        print('빨강 온 !!!!')
        led_red.value(HIGH)                                # 빨강 LED 켜기
    elif (msg == '2'):
        print('빨강 오프 !!!!')
        led_red.value(LOW)                                 # 빨강 LED 끄기
    elif (msg == '3'):
        print('파랑 온 !!!!')
        led_blue.value(HIGH)                               # 파랑 LED 켜기
    elif (msg == '4'):
        print('파랑 오프 !!!!')
        led_blue.value(LOW)                                # 파랑 LED 끄기
    elif (msg == '5'):
        print('초록 온 !!!!')
        led_green.value(HIGH)                              # 초록 LED 켜기
    elif (msg == '6'):
        print('초록 오프 !!!!')
        led_green.value(LOW)                               # 초록 LED 끄기
    elif (msg == '7'):
        print('노랑 온 !!!!')
        led_yellow.value(HIGH)                             # 노랑 LED 켜기
    elif (msg == '8'):
        print('노랑 오프 !!!!')
        led_yellow.value(LOW)                              # 노랑 LED 끄기


# setup
def setup():
    led_red.init(Pin.OUT)                                  # 빨강 LED 출력 모드로 설정
    led_blue.init(Pin.OUT)                                 # 빨강 LED 출력 모드로 설정
    led_green.init(Pin.OUT)                                # 빨강 LED 출력 모드로 설정
    led_yellow.init(Pin.OUT)                               # 빨강 LED 출력 모드로 설정

    print('블루투스 이름 : ' + SerialBT._ble_name)         # 블루투스 이름 출력

    while not (SerialBT.is_connected()):                   # 블루투스 연결 시도
        print('연결되지 않았습니다.')
        time.sleep_ms(1000)        

    print(SerialBT._ble_name + ' : 연결에 성공했습니다.')  # 블루투스가 연결되면 문자열 출력

    SerialBT.on_received(handle_data)                      # 수신받은 데이터를 처리하기 위한 함수 연결


# main loop
def loop():
    pass


if __name__ == "__main__":
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================