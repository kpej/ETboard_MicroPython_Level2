# ******************************************************************************************
# FileName     : 01._servo_motor
# Description  : 서보모터를 지정된 각도만큼 회전 해보기
#                0도 ~ 180도
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
servo = Servo(Pin(D2))                          # 서보모터 핀 지정


# setup
def setup():
    pass


# mainloop
def loop():
    pos = 0
    for x in range(180):                        # 서보모터 시계방향으로 180도 회전
        servo.write_angle(pos)                  #서버모터 각도 설정
        pos += 1
        time.sleep(0.01)                        # 0.01초 대기

    for x in range(180):                        # 서보모터 반시계방향으로 0도 회전
        servo.write_angle(pos)                  #서버모터 각도 설정
        pos -= 1
        time.sleep(0.01)                        # 0.01초 대기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
