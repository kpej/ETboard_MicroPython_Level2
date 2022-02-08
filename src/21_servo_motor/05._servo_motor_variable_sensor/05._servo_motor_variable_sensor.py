# ******************************************************************************************
# FileName     : 05._servo_motor_variable_sensor
# Description  : 가변저항을 돌리면 서보모터가 돌아가는 예제
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     :
# ******************************************************************************************


# import
from machine import Pin
from machine import ADC
from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo


# global variable
servo = Servo(Pin(D2))                          # 서보모터 핀 지정
sensor = ADC(Pin(A0))                           # 가변저항 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)


# mainloop
def loop():
    servo.write_angle(int(sensor.read()/23))    # 가변저항 값을 서보모터 값으로 설정


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
