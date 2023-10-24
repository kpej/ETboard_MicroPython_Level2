# ******************************************************************************************
# FileName     : BluetoothSerial
# Description  : Ble Serial Communication
# Author       : 손철수
# Created Date : 2023.10.24
# Reference    : 그만 배껴라
# Modified     : 
# ******************************************************************************************


# import
import bluetooth
import sys
import time
from .ble_advertising import advertising_payload
from .ble_simple_peripheral import BLESimplePeripheral

# class
class BluetoothSerial(BLESimplePeripheral):
    def __init__(self, name=None):
        self._ble = bluetooth.BLE()
        
        if (name is None):
            self._ble_name = self.make_ble_name()
        elif (len(name) > 8):
            print('Error: 블루투스 이름은 8글자을 넘지 않아야 합니다 !!!')
            sys.exit(1)
        else:
            self._ble_name = name
                
        BLESimplePeripheral.__init__(self, self._ble, self._ble_name)

    def make_ble_name(self):
        self._ble.active(True)
        _add1, _add2 = self._ble.config('mac')
        mac_len = len(_add2)
        if (mac_len != 6):
            print('mac error')
            return None
        #self._ble_name = f'E_{_add2[3]:02X}{_add2[4]:02X}{_add2[5]:02X}'
        return f'E_{_add2[3]:02X}{_add2[4]:02X}{_add2[5]:02X}'
    
    def on_received(self, func):
        super().on_write(func)
   
def demo():    
    p = BluetoothSerial()
    print(p._ble_name)

    def on_rx(v):
        print("RX", v)

    #p.on_write(on_rx)
    p.on_received(on_rx)

    i = 0
    while True:
        if p.is_connected():
            # Short burst of queued notifications .
            for _ in range(3):
                data = str(i) + "_"
                print("TX", data)
                p.send(data)
                i += 1
        time.sleep_ms(100)


if __name__ == "__main__":
    demo()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
