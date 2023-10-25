# ******************************************************************************************
# FileName     : 01._Bluetooth_connect
# Description  : 
# Author       : 손철수
# Created Date : 2023.10.24
# Reference    :
# Modified     : 
# ******************************************************************************************


# import
import time
from ETboard.lib.pin_define import *
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
    

# main loop
def loop():    
    pass


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
