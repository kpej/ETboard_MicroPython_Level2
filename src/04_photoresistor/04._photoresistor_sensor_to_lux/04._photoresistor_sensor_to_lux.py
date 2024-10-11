from machine import ADC, Pin
import time
from ETboard.lib.pin_define import *
from machine import Pin, time_pulse_us


# CDS 센서가 연결된 핀 설정 (ADC 핀)
cds_pin = ADC(Pin(A1))  # ESP32의 경우 ADC 핀 34 사용
cds_pin.atten(ADC.ATTN_11DB)  # 최대 전압 범위 설정 (0-3.3V)

# CDS 값을 Lux로 변환하는 함수
def resistance_to_lux(resistance):
    # 예시로 간단한 변환 식을 사용합니다.
    lux = 500 / (resistance / 1000)
    return lux

while True:
    # CDS 값 읽기 (0-4095)
    sensor_value = cds_pin.read()
    
    # 전압 계산 (ESP32의 경우 3.3V가 최대)
    voltage = sensor_value * (3.3 / 4095.0)
    
    # 저항 계산 (기본 0.1kΩ 저항을 사용한다고 가정)
    resistance = (3.3 - voltage) * (1000)   / voltage
    
    # 저항을 Lux로 변환
    lux = resistance_to_lux(resistance)
    
    print("Resistance: {:.2f} ohms, Lux: {:.2f}".format(resistance, lux))
    
    time.sleep(1)  # 1초 대기
