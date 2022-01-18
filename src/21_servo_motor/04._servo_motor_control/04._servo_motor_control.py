# ******************************************************************************************
# FileName     : 04._servo_motor_control
# Description  : 버튼을 이용해서 서보모터를 제어하는 예제
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin, ADC
from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo


# global variable
servo = Servo(Pin(D2))                         # 서보모터 핀 지정
Up = Pin(D6)                                   # 빨강 버튼 핀 지정
Down = Pin(D9)                                 # 노랑 버튼 핀 지정
pos = 0


# setup
def setup():
    Up.init(Pin.IN)                            # 빨강 버튼 입력모드 설정
    Down.init(Pin.IN)                          # 노랑 버튼 입력모드 설정
    

# mainloop
def loop():
    global pos
    
    Up_state = Up.value()                      # 빨강 버튼값 가져오기
    Down_state = Down.value()                  # 노랑 버튼값 가져오기
    
    if Up_state == 0:                          # 빨강버튼이 눌려질때 서보모터 위로 작동
        pos += 1
        if pos > 180:
            pos = 180
        servo.write_angle(pos)
        time.sleep(0.01)
    
    if Down_state == 0:                        # 노랑버튼이 눌려질때 서보모터 아래로 작동
        pos -= 1
        if pos < 0:
            pos = 0
        servo.write_angle(pos)
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
