# ******************************************************************************************
# FileName     : 03._Bluetooth_two_way_communication
# Description  : 
# Author       : 손철수
# Created Date : 2023.10.24
# Reference    :
# Modified     : 
# ******************************************************************************************


# import
import sys
import time
from ETboard.lib.BluetoothSerial import BluetoothSerial


# global variable
SerialBT = BluetoothSerial()


# setup
def setup():
    print('블루투스 이름 : ' + SerialBT._ble_name)

    while not (SerialBT.is_connected()):
        print('연결되지 않았습니다.')
        time.sleep_ms(1000)        
    
    print(SerialBT._ble_name + ' : 연결에 성공했습니다.')

    SerialBT.on_received(handle_data)
    

# 수신 받은 데이터를 처리
def handle_data(msg):
    print("받은 문자열:", msg)
        

# main loop
def loop():    
    data = input('보낼 문자열을 입력하세요:')
    SerialBT.send(data + '\n')
    time.sleep_ms(20)


# entry point
if __name__ == "__main__":
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
