# ******************************************************************************************
# FileName     : photoresistor_sensor_to_lux.py
# Description  :
# Author       : 손철수
# Created Date : 2024.10.11 : SCS
# Reference    : 2024.10.11 : PEJ : 소스 코드 형식 수정
# ******************************************************************************************


#===========================================================================================
# 기본 모듈 사용하기
#===========================================================================================
from machine import ADC, Pin
import time
from ETboard.lib.pin_define import *
from machine import Pin


#===========================================================================================
# 전역 변수 선언
#===========================================================================================
# CDS 센서가 연결된 핀 설정 (ADC 핀)
cds_pin = ADC(Pin(A1))                                   # ESP32의 경우 ADC 핀 34 사용


#===========================================================================================
def setup():                                             #  설정
#===========================================================================================
    cds_pin.atten(ADC.ATTN_11DB)                         # 최대 전압 범위 설정 (0-3.3V)


#===========================================================================================
def resistance_to_lux(resistance):                       # CDS 값을 Lux로 변환하는 함수
#===========================================================================================
    # 예시로 간단한 변환 식을 사용
    lux = 500 / (resistance / 1000)
    return lux


#===========================================================================================
def loop():                                              #  반복 처리
#===========================================================================================
    sensor_value = cds_pin.read()                        # CDS 값 읽기 (0 - 4095)

    # 전압 계산 (ESP32의 경우 3.3V가 최대)
    voltage = sensor_value * (3.3 / 4095.0)

    # 저항 계산 (기본 0.1kΩ 저항을 사용한다고 가정)
    resistance = (3.3 - voltage) * (1000) / voltage

    lux = resistance_to_lux(resistance)                  # 저항을 Lux로 변환

    print("Resistance: {:.2f} ohms, Lux: {:.2f}".format(resistance, lux))

    time.sleep(1)  # 1초 대기


#===========================================================================================
# 시작 지점
#===========================================================================================
if __name__ == "__main__":
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================