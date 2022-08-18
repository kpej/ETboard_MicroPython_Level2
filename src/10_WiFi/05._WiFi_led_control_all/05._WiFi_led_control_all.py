# ******************************************************************************************
# FileName     : 05._WiFi_led_control
# Description  : 와이파이를 이용해 4개의 LED를 껐다 켰다하는 웹서버 만들어 보기
# Author       : 손정인
# Created Date : 2022.02.08
# Reference    :
# Modified     : 
# ******************************************************************************************

#import
import time
from machine import Pin, ADC
import ETboard.lib.WiFi as WiFi
from ETboard.lib.pin_define import *

# global variable
ssid = "ssid"                                  # 와이파이 아이디 입력
password = "password"                          # 와이파이 비밀번호 입력
server = WiFi.WebServer(80)                    # 서버에서 사용할 포트 설정
led_red = Pin(D2)                              # 빨강 LED 의 핀 번호 지정
led_blue = Pin(D3)                             # 파랑 LED 의 핀 번호 지정
led_green = Pin(D4)                            # 초록 LED 의 핀 번호 지정
led_yellow = Pin(D5)                           # 노랑 LED 의 핀 번호 지정
html_page = "<font size=16>Click <a href=\"/red_led_on\"> red On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/red_led_off\"> red Off</a> to turn Off LED<br></font>"\
            "<font size=16>Click <a href=\"/blue_led_on\"> blue On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/blue_led_off\"> blue Off</a> to turn Off LED<br></font>"\
            "<font size=16>Click <a href=\"/green_led_on\"> green On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/green_led_off\"> green Off</a> to turn Off LED<br></font>"\
            "<font size=16>Click <a href=\"/yellow_led_on\"> yellow On </a> to turn On LED<br></font>"\
            "<font size=16>Click <a href=\"/yellow_led_off\"> yellow Off</a> to turn Off LED<br></font>"
 
# user function
def handle_root() :                            # root(/)로 접속했을 때 처리하는 함수
    led_red.value(HIGH)                        # 빨강 LED 켜기
    print("root call!")                        # 페이지로 접속했다고 알려줌
    server.send(200, "text/html", html_page)
    led_red.value(LOW)

def handle_d2on() :                            # red_led_on(/red_led_on)로 접속했을 때 처리하는 함수
    print("D2 On call!")
    led_red.value(HIGH)                        # 빨강 LED 켜기
    server.send(200, "text/html", html_page)

def handle_d2off() :                           # red_led_off(/red_led_off)로 접속했을 때 처리하는 함수
    print("D2 Off call!")                      # 페이지로 접속했다고 알려줌
    led_red.value(LOW)
    server.send(200, "text/html", html_page)

def handle_d3on() :                            # blue_led_on(/blue_led_on)로 접속했을 때 처리하는 함수
    print("D3 On call!")
    led_blue.value(HIGH)                       # 파랑 LED 켜기
    server.send(200, "text/html", html_page)

def handle_d3off() :                           #blue_led_off(/blue_led_off)로 접속했을 때 처리하는 함수
    print("D3 Off call!")                      # 페이지로 접속했다고 알려줌
    led_blue.value(LOW)
    server.send(200, "text/html", html_page)

def handle_d4on() :                            # green_led_on(/green_led_on)로 접속했을 때 처리하는 함수
    print("D4 On call!")
    led_green.value(HIGH)                      # 초록 LED 켜기
    server.send(200, "text/html", html_page)

def handle_d4off() :                           #green_led_off(/green_led_off)로 접속했을 때 처리하는 함수
    print("D4 Off call!")                      # 페이지로 접속했다고 알려줌
    led_green.value(LOW)
    server.send(200, "text/html", html_page)

def handle_d5on() :                            # yellow_led_on(/yellow_led_on)로 접속했을 때 처리하는 함수
    print("D5 On call!")
    led_yellow.value(HIGH)                     # 노랑 LED 켜기
    server.send(200, "text/html", html_page)

def handle_d5off() :                           # yellow_led_off(/yellow_led_off)로 접속했을 때 처리하는 함수
    print("D5 Off call!")                      # 페이지로 접속했다고 알려줌
    led_yellow.value(LOW)
    server.send(200, "text/html", html_page)

# setup
def setup() :
    led_red.init(Pin.OUT)                      # 빨강 LED 를 출력상태로 설정
    led_blue.init(Pin.OUT)                     # 파랑 LED 를 출력상태로 설정
    led_green.init(Pin.OUT)                    # 초록 LED 를 출력상태로 설정
    led_yellow.init(Pin.OUT)                   # 노랑 LED 를 출력상태로 설정
    WiFi.begin(ssid, password)                 # WiFi에 접속을 시도
    
    while WiFi.status() != WiFi.WL_CONNECTED : # 연결이 될 때까지 계속 대기
        time.sleep(0.5)
        print(".")
    
    print("")
    print("WiFi connected")
    print("IP address : ")
    print(WiFi.localIP())                      # 연결이 됐다면 할당받은 아이피를 출력함
    
    server.on("/", handle_root)                # root(/)로 접속했을 때 처리하는 함수랑 연결
    server.on("/red_led_on", handle_d2on)      # red_led_on(/red_led_on)로 접속했을 때 처리하는 함수랑 연결
    server.on("/red_led_off", handle_d2off)    # red_led_off(/red_led_off)로 접속했을 때 처리하는 함수랑 연결
    server.on("/blue_led_on", handle_d3on)     # blue_led_on(/blue_led_on)로 접속했을 때 처리하는 함수랑 연결
    server.on("/blue_led_off", handle_d3off)   # blue_led_off(/blue_led_off)로 접속했을 때 처리하는 함수랑 연결
    server.on("/green_led_on", handle_d4on)    # green_led_on(/green_led_on)로 접속했을 때 처리하는 함수랑 연결
    server.on("/green_led_off", handle_d4off)  # green_led_off(/green_led_off)로 접속했을 때 처리하는 함수랑 연결
    server.on("/yellow_led_on", handle_d5on)   # yellow_led_on(/yellow_led_on)로 접속했을 때 처리하는 함수랑 연결
    server.on("/yellow_led_off", handle_d5off) # yellow_led_off(/yellow_led_off)로 접속했을 때 처리하는 함수랑 연결
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
