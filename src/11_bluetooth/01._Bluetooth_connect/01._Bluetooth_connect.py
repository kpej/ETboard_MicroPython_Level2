# ******************************************************************************************
# FileName     : 01._Bluetooth_connect
# Description  : 이티보드에 블루투스 연결해 보기
# Author       : 손철수
# Created Date : 2023.10.24
# Reference    :
# Modified     : 2023.10.25 : PEJ : 헤더 Description 추가, 주석 추가
# ******************************************************************************************


# import
import time
from ETboard.lib.BluetoothSerial import BluetoothSerial


# global variable
SerialBT = BluetoothSerial()


# setup
def setup():
    print('블루투스 이름 : ' + SerialBT._ble_name)          # 블루투스 이름 출력

    while not (SerialBT.is_connected()):                    # 블루투스 연결 시도
        print('연결되지 않았습니다.')
        time.sleep_ms(1000)        

    print(SerialBT._ble_name + ' : 연결에 성공했습니다.')   # 블루투스가 연결되면 문자열 출력


# main loop
def loop():    
    pass                                                    # pass를 사용하여 건너뜀


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