# ******************************************************************************************
# FileName     : 02._servo_motor_timer
# Description  : 서보모터 회전 해보기
#                0도, 180도
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 주석 수정
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo


# global variable
servo = Servo(Pin(D6))                         # 서보모터 핀 지정


# setup
def setup():
    pass


# mainloop
def loop():
    servo.write_angle(180)                     # 서보모터 180도까지 회전
    time.sleep(2)                              # 2초 대기
    
    servo.write_angle(0)                       # 서보모터 0도까지 회전
    time.sleep(2)                              # 2초 대기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
