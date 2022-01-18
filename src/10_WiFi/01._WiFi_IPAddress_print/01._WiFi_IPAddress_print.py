# ******************************************************************************************
# FileName     : 01._WiFi_IPAddress_print
# Description  : WiFi에 연결하고 받은 IP주소를 출력하는 예제
# Author       : 위대원
# Created Date : 2021.08.24
# Reference    :
# modified     :
# ******************************************************************************************


# import
import time
import ETboard.lib.WiFi as WiFi


# global variable
ssid = "ssid"                                   # 와이파이 아이디
password = "password"                           # 와이파이 비밀번호


# setup
def setup():
    WiFi.begin(ssid, password)                  # ssid 와 password 를 이용해서 와이파이에 접속을 시도
    while WiFi.status() != WiFi.WL_CONNECTED:   # 연결이 될 때까지 계속 대기
        time.sleep(0.5)                         # 0.5초 기다리기
        print(".")
        
    print("")
    print("WiFi connected")
    print("IP address : ")
    print(WiFi.localIP())                       # 연결이 됐다면 할당받은 아이피를 출력함


# main loop
def loop():
    pass

    
if __name__ == "__main__":
    setup()
    while True:
        loop()
    
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
    
