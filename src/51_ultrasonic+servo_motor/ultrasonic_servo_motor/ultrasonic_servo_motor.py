# ******************************************************************************************
# FileName     : ultrasonic_servo_motor
# Description  : 측정된 물체가 일정거리안에 들어오면 서보모터를 올려주고(180도)
#                일정 거리에서 벗어나면 서보모터를 다시 내려주는(0도) 예제
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo


# global variable
servo = Servo(Pin(D2))                           # 서보모터 핀 지정
trigPin = Pin(D9)                                # 초음파 송신부 핀 지정
echoPin = Pin(D8)                                # 초음파 수신부 핀 지정


# setup
def setup():
    trigPin.init(Pin.OUT)                        # 초음파 송신부 출력모드 설정
    echoPin.init(Pin.IN)                         # 초음파 수신부 입력모드 설정
    

# main loop
def loop():
    trigPin.value(LOW)
    echoPin.value(LOW)
    time.sleep_ms(2)
    trigPin.value(HIGH)
    time.sleep_ms(10)
    trigPin.value(LOW)

    duration = time_pulse_us(echoPin, HIGH)
    distance = 17 * duration / 1000
    
    if distance <= 20:                           # 거리가 20 이하이면 180도로 맞춘다.
        servo.write_angle(180)
    
    if distance > 20:                            # 거리가 20 초과이면 0도로 맞춘다
        servo.write_angle(0)
        

if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
