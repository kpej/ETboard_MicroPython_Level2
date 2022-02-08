# ******************************************************************************************
# FileName     : 01._servo_motor
# Description  : 서보모터를 사용하는 기본적인 예제
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
servo = Servo(Pin(D2))                          # 서보모터 핀 지정


# setup
def setup():
    pass


# mainloop
def loop():
    pos = 0
    for x in range(180):                        # 서보모터 시계방향으로 180도 회전
        servo.write_angle(pos)
        pos += 1
        time.sleep(0.01)
        
    for x in range(180):                        # 서보모터 반시계방향으로 0도 회전
        servo.write_angle(pos)
        pos -= 1
        time.sleep(0.01)


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
