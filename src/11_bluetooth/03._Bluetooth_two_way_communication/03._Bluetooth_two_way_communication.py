# ******************************************************************************************
# FileName     : 03._Bluetooth_two_way_communication
# Description  : PC와 블루투스로 연결된 기기간 블루투스 통신해 보기
# Author       : 손철수
# Created Date : 2023.10.24
# Reference    :
# Modified     : 2023.10.25 : PEJ : 헤더 Description 추가
# ******************************************************************************************


# import
import sys
import time
from ETboard.lib.BluetoothSerial import BluetoothSerial


# global variable
SerialBT = BluetoothSerial()


# 수신 받은 데이터를 처리
def handle_data(msg):
    print("받은 문자열:", msg)                              # 수신받은 데이터를 쉘에 출력


# setup
def setup():
    print('블루투스 이름 : ' + SerialBT._ble_name)          # 블루투스 이름 출력

    while not (SerialBT.is_connected()):                    # 블루투스 연결 시도
        print('연결되지 않았습니다.')
        time.sleep_ms(1000)        

    print(SerialBT._ble_name + ' : 연결에 성공했습니다.')   # 블루투스가 연결되면 문자열 출력

    SerialBT.on_received(handle_data)                       # 수신받은 데이터를 처리하기 위한 함수 연결


# main loop
def loop():
    data = input('보낼 문자열을 입력하세요:')               # 데이터를 입력받음
    SerialBT.send(data + '\n')                              # 입력받은 데이터를 전송
    time.sleep_ms(20)


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