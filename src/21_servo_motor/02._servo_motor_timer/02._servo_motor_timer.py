# ******************************************************************************************
# FileName     : 02._servo_motor_timer
# Description  : 서보모터가 일정 시간 마다 up, down 하는 예제
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo


# global variable
servo = Servo(Pin(D2))                         # 서보모터 핀 지정


# setup
def setup():
    pass


# mainloop
def loop():
    servo.write_angle(180)                     # 서보모터 180 작동
    time.sleep(2)                              # 2초 기다리기
    
    servo.write_angle(0)                       # 서보모터 0 작동
    time.sleep(2)                              # 2초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
