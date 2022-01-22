# ******************************************************************************************
# FileName     : 02._WiFi_simple_web_server
# Description  : 간단한 문자열을 보여주는 서버의 예제
# Author       : 위대원
# Created Date : 2021.08.24
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin
import ETboard.lib.WiFi as WiFi
from ETboard.lib.pin_define import *


# global variable
ssid = "ssid"                                   # 와이파이 아이디
password = "password"                           # 와이파이 비밀번호
server = WiFi.WebServer(80)
led = Pin(D2)                                   # 빨강 LED 의 핀 번호 지정


# user function
def handle_root():
    led.value(HIGH)                             # LED 를 키기
    server.send(200, "text/plain", "hello from ET-board! __ {}".format(time.time()))
    led.value(LOW)                              # LED 를 끄기


# setup
def setup():
    led.init(Pin.OUT)                           # LED 를 출력상태로 설정
    WiFi.begin(ssid, password)                  # ssid 와 password 를 이용해서 와이파이에 접속을 시도
    
    while WiFi.status() != WiFi.WL_CONNECTED:   # 연결이 될 때까지 계속 대기
        time.sleep(0.5)                         # 0.5초 대기
        print(".")
        
    print("")
    print("WiFi connected")
    print("IP address : ")
    print(WiFi.localIP())                       # 연결이 됐다면 할당받은 아이피를 출력함
    
    server.on("/", handle_root)                 # root(/)로 접속했을 때 처리하는 함수랑 연결
    server.begin()                              # 서버 시작
    

# main loop
def loop():
    server.handleClient()                       # 클라이언트의 접속을 받음
    print("loop run...")
    time.sleep(0.02)                            # 0.02초 대기
    
    
if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
