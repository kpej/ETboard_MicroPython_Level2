# ******************************************************************************************
# FileName     : 03._WiFi_web_server_variable_resistance
# Description  : 웹서버에서 가변저항의 값을 볼 수 있는 예제
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
sensor = ADC(Pin(A0))                          # 가변 저항 핀 번호


# user function
def handle_root():                             # root(/)로 접속했을 때 처리하는 함수
    led.value(HIGH)                            # 빨강 LED 를 켜기
    print("root call!")                        # 페이지로 접속했다고 알려줌
    server.send(200, "text/plain", "hello from ET-board! __ {}".format(time.time()))
    led.value(LOW)                             # 빨강 LED 를 끄기
    

def handle_a0():                               # read_a0(/read_a0)로 접속했을 때 처리하는 함수
    sensor_value = sensor.read()
    send_data = "variable_resistance : "       # 가변 저항의 값을 읽어옴
    send_data = send_data + str(sensor_value)  # 단순 문자열 저장
    print("A0 call!")                          # 페이지로 접속했다고 알려줌
    server.send(200, "text/plain", send_data)


# setup
def setup():
    led.init(Pin.OUT)                          # LED 를 출력상태로 설정
    sensor.atten(ADC.ATTN_11DB)
    WiFi.begin(ssid, password)                 # ssid 와 password 를 이용해서 와이파이에 접속을 시도
    
    while WiFi.status() != WiFi.WL_CONNECTED:  # 연결이 될 때까지 계속 대기
        time.sleep(0.5)
        print(".")
        
    print("")
    print("WiFi connected")
    print("IP address : ")
    print(WiFi.localIP())                      # 연결이 됐다면 할당받은 아이피 풀력
    
    server.on("/", handle_root)                # root(/)로 접속했을 때 처리하는 함수랑 연결
    server.on("/read_a0", handle_a0)           # read_a0(/read_a0)
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
