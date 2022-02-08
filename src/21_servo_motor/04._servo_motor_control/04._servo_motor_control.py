# ******************************************************************************************
# FileName     : 04._servo_motor_control
# Description  : 발강, 노랑 버튼을 눌러 서보모터를 제어 해보기
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 주석 수정, 소스 크린징
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
    
    if Up_state == LOW:                        # 빨강 버튼이 눌리면 서보모터의 각도 1도씩 증가
        pos += 1
        if pos > 180:
            pos = 180                          # 서보모터의 각도가 180도 이상이 되지 않게 설정
        servo.write_angle(pos)
        time.sleep(0.01)
    
    if Down_state == LOW:                      # 노랑 버튼이 눌리면 서보모터의 각도 1도씩 감소
        pos -= 1
        if pos < 0:
            pos = 0                            # 서보모터의 각도가 0도 이하가 되지 않게 설정
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
