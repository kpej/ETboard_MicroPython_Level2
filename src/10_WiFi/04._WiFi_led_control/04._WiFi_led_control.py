# ******************************************************************************************
# FileName     : 04._WiFi_led_control
# Description  : html 페이지에서 버튼을 누르면 LED 를 켜고 끌 수 있는 예제
# Author       : 위대원
# Created Date : 2021.08.24
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin, ADC
import ETboard.lib.WiFi as WiFi
from ETboard.lib.pin_define import *


# global variable
ssid = "ssid"                                  # 와이파이 아이디
password = "password"                          # 와이파이 비밀번호
server = WiFi.WebServer(80)                    # 서버에서 사용할 포트 설정
led = Pin(D2)                                  # 빨강 LED 의 핀 번호 지정
html_page = "<font size=16>Click <a href=\"/red_led_on\"> red On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/red_led_off\"> red Off</a> to turn Off LED<br></font>"


# user function
def handle_root():                             # root(/)로 접속했을 때 처리하는 함수
    led.value(HIGH)                            # 빨강 LED 켜기
    print("root call!")                        # 페이지로 접속했다고 알려줌
    server.send(200, "text/html", html_page)
    led.value(LOW)
    

def handle_d2on():                             # red_led_on(/red_led_on)로 접속했을 때 처리하는 함수
    print("D2 On call!")
    led.value(HIGH)                            # 빨강 LED 켜기
    server.send(200, "text/html", html_page)
    
    
def handle_d2off():                            # red_led_off(/red_led_off)로 접속했을 때 처리하는 함수
    print("D2 Off call!")                      # 페이지로 접속했다고 알려줌
    led.value(LOW)
    server.send(200, "text/html", html_page)


# setup
def setup():
    led.init(Pin.OUT)                          # 빨강 LED 를 출력상태로 설정
    WiFi.begin(ssid, password)                 # WiFi에 접속을 시도
    
    while WiFi.status() != WiFi.WL_CONNECTED:  # 연결이 될 때까지 계속 대기
        time.sleep(0.5)
        print(".")
        
    print("")
    print("WiFi connected")
    print("IP address : ")
    print(WiFi.localIP())                      # 연결이 됐다면 할당받은 아이피를 출력함
    
    server.on("/", handle_root)                # root(/)로 접속했을 때 처리하는 함수랑 연결
    server.on("/red_led_on", handle_d2on)      # red_led_on(/red_led_on)로 접속했을 때 처리하는 함수랑 연결
    server.on("/red_led_off", handle_d2off)    # red_led_off(/red_led_off)로 접속했을 때 처리하는 함수랑 연결
    server.begin()                             # 서버 시작
    

# main loop
def loop():
    server.handleClient()                      # 클라이언트의 접속을 받음
    print("loop run...")
    time.sleep(0.02)
    
    
if __name__ == "__main__":
    setup()
    while True:
        loop()
    
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
