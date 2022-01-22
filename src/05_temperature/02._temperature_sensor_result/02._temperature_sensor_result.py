# ******************************************************************************************
# FileName     : 02._temperature_sensor_result
# Description  : 온도센서 값을 이용해 온도 출력 해보기
# Author       : 이승찬
# Created Date : 2021.08.17
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
import math
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# global variable
R1 = 10000
c1 = 1.009249522e-03
c2 = 2.378405444e-04
c3 = 2.019202697e-07

sensor = ADC(Pin(A2))                          # 온도센서 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)                # 온도센서 입력모드 설정


# main loop
def loop():
    Vo = sensor.read()                         # 온도센서 값 저장

    # 온도 센서 값을 이용하여 실제 온도 값 으로 변환
    R2 = R1 * (4095.0 / Vo - 1.0)
    logR2 = math.log(R2)
    T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2))
    Tc = T - 273.15
    
    print(Tc)                                  # 온도 변환 값 출력
    
    time.sleep(0.1)                            # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
