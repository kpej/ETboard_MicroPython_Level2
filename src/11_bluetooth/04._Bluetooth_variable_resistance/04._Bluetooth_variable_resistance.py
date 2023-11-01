# ******************************************************************************************
# FileName     : 04._Bluetooth_variable_resistance
# Description  : 
# Author       : 손철수
# Created Date : 2023.10.25
# Reference    :
# Modified     : 2023.10.25 : PEJ : 헤더 Description 추가, 주석 추가
# ******************************************************************************************


# import
import sys
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *
from ETboard.lib.BluetoothSerial import BluetoothSerial


# global variable
sensor = ADC(Pin(A0))                                      # 가변저항 핀 지정
SerialBT = BluetoothSerial()


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)                            # 가변저항 입력 모드 설정

    print('블루투스 이름 : ' + SerialBT._ble_name)         # 블루투스 이름 출력

    while not (SerialBT.is_connected()):                   # 블루투스 연결 시도
        print('연결되지 않았습니다.')
        time.sleep_ms(1000)        

    print(SerialBT._ble_name + ' : 연결에 성공했습니다.')  # 블루투스가 연결되면 문자열 출력


# main loop
def loop():    
    sensor_result = sensor.read()                           # 가변저항 센서 값 저장
    print(sensor_result)                                    # 가변저항 센서 값 출력
    SerialBT.send(str(sensor_result)+'\n')                  # 가변저항 센서 값 전송
    time.sleep_ms(1000)


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