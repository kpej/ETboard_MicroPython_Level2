# ******************************************************************************************
# FileName     : 04._Bluetooth_analog_sensor
# Description  : 블루투스 통신으로 아날로그 센서 값 전송해 보기
# Author       : 손철수
# Created Date : 2023.10.25
# Reference    :
# Modified     : 2023.10.25 : PEJ : 헤더 Description 추가, 주석 추가
# Modified     : 2024.07.19 : PEJ : 라이브러리 경로 수정, 블루투스 연결 확인문 추가
# Modified     : 2024.07.19 : PEJ : 조도 센서, 온도 센서 추가
# ******************************************************************************************


#import
import sys                                               # 시스템 관련 라이브러리
import time                                              # 시간 관련 라이브러리
from machine import ADC, Pin                             # 핀 관련 라이브러리
from ETboard.lib.pin_define import *                     # 이티보드 핀 관련 라이브러리
from BluetoothSerial import BluetoothSerial              # 블루투스 통신 관련 라이브러리


# global variable
sensor1 = ADC(Pin(A0))                                   # 가변저항 핀 지정
sensor2 = ADC(Pin(A1))                                   # 조도 센서 핀 지정
sensor3 = ADC(Pin(A2))                                   # 온도 센서 핀 지정

SerialBT = BluetoothSerial()                             # 블루투스 통신 설정


# setup
def setup():
    sensor1.atten(ADC.ATTN_11DB)                         # 가변저항 입력 모드 설정
    sensor2.atten(ADC.ATTN_11DB)                         # 조도 센서 입력 모드 설정
    sensor3.atten(ADC.ATTN_11DB)                         # 온도 센서 입력 모드 설정

    print('블루투스 이름 : ' + SerialBT._ble_name)       # 블루투스 이름 출력


# main loop
def loop():
    if not SerialBT.is_connected():                      # 블루투스가 연결되지 않았다면
        print('연결되지 않았습니다.')                    # 쉘에 "연결되지 않았습니다." 출력
        time.sleep(1)
        return

    topic_msg = "T:/et/smpl/tele/sensor"
    print(topic_msg)
    SerialBT.send(topic_msg + '\n')

    sensor_result = sensor1.read()                       # 가변저항 값 저장
    data_msg = 'D:{"VR":' + str(sensor_result) + "}"     # 가변저항 값 메시지 저장
    print(data_msg)
    SerialBT.send(data_msg+'\n')                         # 가변저항 값 메시지 전송

    topic_msg = "T:/et/smpl/tele/sensor"
    print(topic_msg)
    SerialBT.send(topic_msg + '\n')

    sensor_result = sensor2.read()                       # 조도 센서 값 저장
    data_msg = 'D:{"CDS":' + str(sensor_result) + "}"    # 조도 센서 값 메시지 저장
    print(data_msg)                                   
    SerialBT.send(data_msg+'\n')                         # 조도 센서 값 메시지 전송

    topic_msg = "T:/et/smpl/tele/sensor"
    print(topic_msg)
    SerialBT.send(topic_msg + '\n')

    sensor_result = sensor3.read()                       # 온도 센서 값 저장
    data_msg = 'D:{"TEMP":' + str(sensor_result) + "}"   # 온도 센서 값 메시지 저장
    print(data_msg)                                   
    SerialBT.send(data_msg+'\n')                         # 온도 센서 값 메시지 전송

    time.sleep(1)


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