# ******************************************************************************************
# FileName     : 04._Bluetooth_variable_resistance
# Description  : 
# Author       : 손철수
# Created Date : 2023.10.25
# Reference    :
# Modified     : 
# ******************************************************************************************


# import
import sys
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *
from ETboard.lib.BluetoothSerial import BluetoothSerial


# global variable
sensor = ADC(Pin(A0))                 # 가변저항 핀 지정
SerialBT = BluetoothSerial()

# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)       # 가변저항 입력 모드 설정
    
    print('블루투스 이름 : ' + SerialBT._ble_name)

    while not (SerialBT.is_connected()):
        print('연결되지 않았습니다.')
        time.sleep_ms(1000)        
    
    print(SerialBT._ble_name + ' : 연결에 성공했습니다.')
    

# main loop
def loop():    
    sensor_result = sensor.read()     # 가변저항 센서 값 저장
    print(sensor_result)              # 가변저항 센서 값 출력
    SerialBT.send(str(sensor_result)+'\n')
    time.sleep_ms(1000)


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
