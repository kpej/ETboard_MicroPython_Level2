# ******************************************************************************************
# FileName     : 05._Bluetooth_led_control
# Description  : 블루투스 통신으로 LED 제어해 보기
# Author       : 손철수
# Created Date : 2023.10.25
# Reference    :
# Modified     : 2023.10.25 : PEJ : 헤더, 푸터 주석 추가, 코드 주석 추가, 파일명 변경
# Modified     : 2024.07.19 : PEJ : 라이브러리 경로 수정, 블루투스 연결 확인문 추가
# ******************************************************************************************


#import
import sys                                               # 시스템 관련 라이브러리
import time                                              # 시간 관련 라이브러리
from machine import Pin                                  # 핀 관련 라이브러리
from ETboard.lib.pin_define import *                     # 이티보드 핀 관련 라이브러리
from BluetoothSerial import BluetoothSerial              # 블루투스 통신 관련 라이브러리


# global variable
led_red = Pin(D2)                                        # 빨강 LED 핀 지정
led_blue = Pin(D3)                                       # 파랑 LED 핀 지정
led_green = Pin(D4)                                      # 초록 LED 핀 지정
led_yellow = Pin(D5)                                     # 노랑 LED 핀 지정

SerialBT = BluetoothSerial()                             # 블루투스 통신 설정


# 수신 받은 데이터를 처리
def handle_data(msg):
    msg_str = str(msg, 'UTF-8')
    print("받은 문자열:", msg_str)                       # 수신받은 데이터를 쉘에 출력

    if (msg_str == 'RBON'):                              # 수신받은 데이터가 "RBON"이라면
        print('빨강 LED 켜기')                           # 빨강 LED 켜기
        led_red.value(HIGH)
    elif (msg_str == 'RBOFF'):                           # 수신받은 데이터가 "RBOFF"라면
        print('빨강 LED 끄기')                           # 빨강 LED 끄기
        led_red.value(LOW)
    elif (msg_str == 'BBON'):                            # 수신받은 데이터가 "BBON"이라면
        print('파랑 LED 켜기')                           # 파랑 LED 켜기
        led_blue.value(HIGH)
    elif (msg_str == 'BBOFF'):                           # 수신받은 데이터가 "BBOFF"라면
        print('파랑 LED 끄기')                           # 파랑 LED 끄기
        led_blue.value(LOW)
    elif (msg_str == 'GBON'):                            # 수신받은 데이터가 "GBON"이라면
        print('초록 LED 켜기')                           # 초록 LED 켜기
        led_green.value(HIGH)
    elif (msg_str == 'GBOFF'):                           # 수신받은 데이터가 "GBOFF"라면
        print('초록 LED 끄기')                           # 초록 LED 끄기
        led_green.value(LOW)
    elif (msg_str == 'YBON'):                            # 수신받은 데이터가 "YBON"이라면
        print('노랑 LED 켜기')                           # 노랑 LED 켜기
        led_yellow.value(HIGH)
    elif (msg_str == 'YBOFF'):                           # 수신받은 데이터가 "YBOFF"라면
        print('노랑 LED 끄기')                           # 노랑 LED 끄기
        led_yellow.value(LOW)


# setup
def setup():
    led_red.init(Pin.OUT)                                # 빨강 LED 출력 모드로 설정
    led_blue.init(Pin.OUT)                               # 파랑 LED 출력 모드로 설정
    led_green.init(Pin.OUT)                              # 초록 LED 출력 모드로 설정
    led_yellow.init(Pin.OUT)                             # 노랑 LED 출력 모드로 설정

    print('블루투스 이름 : ' + SerialBT._ble_name)       # 블루투스 이름 출력

    SerialBT.on_received(handle_data)                    # 수신받은 데이터를 처리하기 위한 함수 연결


# main loop
def loop():
    if not SerialBT.is_connected():                      # 블루투스가 연결되지 않았다면
        print('연결되지 않았습니다.')                    # 쉘에 "연결되지 않았습니다." 출력
        time.sleep(1)
        return


# start point
if __name__ == "__main__":
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================