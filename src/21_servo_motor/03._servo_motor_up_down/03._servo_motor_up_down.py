# ******************************************************************************************
# FileName     : 03._servo_motor_up_down
# Description  : up 버튼을 누르면 서보모터를 180도까지 회전하고 (빨강버튼)
#                down 버튼을 누르면 0도까지 회전함            (노랑버튼)
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
Up = Pin(D6)                                   # 빨강 버튼 핀 지정
Down = Pin(D9)                                 # 노랑 버튼 핀 지정


# setup
def setup():
    Up.init(Pin.IN)                            # 빨강 버튼 입력모드 설정
    Down.init(Pin.IN)                          # 노랑 버튼 입력모드 설정


# mainloop
def loop():
    Up_state = Up.value()                      # 빨강 버튼값 가져오기
    Down_state = Down.value()                  # 노랑 버튼값 가져오기
    
    if Up_state == 0:                          # 뻘강 버튼이 눌리면 서보모터 위로 작동
        servo.write_angle(180)
        time.sleep(0.3)
                
    if Down_state == 0:                        # 노랑 버튼이 눌리면 서보모터 아래로 작동
        servo.write_angle(0)
        time.sleep(0.3)


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
