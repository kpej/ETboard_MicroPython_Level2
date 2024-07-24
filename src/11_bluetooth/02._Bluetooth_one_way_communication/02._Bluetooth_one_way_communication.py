# ******************************************************************************************
# FileName     : 02._Bluetooth_one_way_communication
# Description  : PC에서 데이터를 입력받아 블루투스를 통해 메시지 전송해 보기
# Author       : 손철수
# Created Date : 2023.10.24
# Reference    :
# Modified     : 2023.10.25 : PEJ : 헤더 Description 추가, 주석 추가
# Modified     : 2024.07.19 : PEJ : 라이브러리 경로 수정, 블루투스 연결 확인문 추가
# ******************************************************************************************


#import
import sys                                               # 시스템 관련 라이브러리
import time                                              # 시간 관련 라이브러리
from BluetoothSerial import BluetoothSerial              # 블루투스 통신 관련 라이브러리


# global variable
SerialBT = BluetoothSerial()                             # 블루투스 통신 설정


# setup
def setup():
    print('블루투스 이름 : ' + SerialBT._ble_name)       # 블루투스 이름 출력


# main loop
def loop():
    if not SerialBT.is_connected():                      # 블루투스가 연결되지 않았다면
        print('연결되지 않았습니다.')                    # 쉘에 "연결되지 않았습니다." 출력
        time.sleep(1)
        return
        
    data = input('보낼 문자열을 입력하세요:')            # 데이터를 입력받음
    SerialBT.send(data + '\n')                           # 입력받은 데이터를 전송


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