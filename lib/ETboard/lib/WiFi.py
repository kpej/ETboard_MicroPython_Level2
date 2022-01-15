# ********************************************************************************
# FileName: WiFi
# Description : 소켓 모듈의 래퍼 모듈
# Author : 위대원
# Created Date : 2021.08.24
# Reference :
# modified :
# ********************************************************************************


# import
import network
import time
import gc
try:
    import usocket as socket
except:
    import socket


# global function
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.disconnect()

WL_CONNECTED = True
WL_DISCONNECTED = False


def get_ap_list() -> list:
    """
    :return: ap list [(ssid, rssi, authmode, hidden), (ssid, rssi, authmode, hidden)]
    """

    global wlan
    ap_list = wlan.scan()
    
    new_ap_list = []
    for ssid, bssid, channel, rssi, authmode, hidden in ap_list:
        new_ap_list.append((ssid.decode("utf-8")
                            , rssi
                            , authmode
                            , hidden))
        
    return new_ap_list


def get_wifi_list() -> list:
    """
    get_ap_list Wrapper
    :return: ap list [(ssid, RSSI, authmode, hidden), (ssid, RSSI, authmode, hidden)]
    """

    return get_ap_list()


def isconnected():
    """
    check wifi connect
    :return: bool, connect = True
    """

    global wlan
    return wlan.isconnected()


def get_connect_info() -> tuple:
    """
    get wifi connect info
    :return: tuple (ip_address, subnet, gateway, dns)
    """

    global wlan
    return wlan.ifconfig()


def get_ip() -> str:
    """
    if wifi connected return ip address
    :return: str ip address
    """

    return get_connect_info()[0]


def localIP() -> str:
    """
    get_ip Wrapper
    :return: str ip address
    """

    return get_ip()


def get_subnet() -> str:
    """
    if wifi connected return subnet mask
    :return: str subnet mask
    """

    return get_connect_info()[1]


def get_gateway() -> str:
    """
    if wifi connected return gateway addr
    :return: str gateway addr
    """

    return get_connect_info()[2]


def get_dns() -> str:
    """
    if wifi connected return dns addr
    :return: str dns addr
    """

    return get_connect_info()[3]


def get_mac() -> str:
    """
    etboard mac address
    :return: str mac addr
    """

    global wlan
    return wlan.config("mac")


def connect(ssid: str, password: str, time_out: int = 5000) -> bool:
    """
    wifi connect
    :param ssid: target ssid
    :param password: ssid password
    :param time_out: connect time out
    :return: connect success True, Fail False
    """

    global wlan
    wlan.connect(ssid, password)
    
    start_time = time.ticks_ms()
    while not isconnected():
        if time.ticks_ms() - start_time > time_out:
            break

    return True if isconnected() else False


def disconnect() -> None:
    """
    wifi disconnect
    :return: None
    """

    global wlan
    wlan.disconnect()
    

def begin(ssid: str, password: str) -> None:
    """
    connect Wrapper function
    :param ssid: target ssid
    :param password: ssid password
    :return: None
    """

    connect(ssid, password)
    
    
def status() -> bool:
    """
    get wifi connect status
    :return: if connect success True, disconnect False
    """

    return isconnected()


class WebServer:
    def __init__(self, port: int = 80):
        """
        init object
        :param port: int bind port number
        """

        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(1)
        self.handle_dict = dict()
        self.last_client = None
    
    def __del__(self):
        """
        dispose object
        close sock
        """

        self.sock.close()
    
    def begin(self) -> None:
        """
        init socket (bind, listen)
        :return: None
        """

        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("", self.port))
        self.sock.listen(5)
        
    def on(self, route: str, handler: object) -> None:
        """
        webserve route handler
        :param route: str route name
        :param handler: object handler function
        :return: None
        """

        self.handle_dict[route] = handler
        
    def send(self, code: int, content_type: str, content: str) -> None:
        enter_code = chr(10)
        self.last_client.send('HTTP/1.1 {} OK{}'.format(code, enter_code))
        self.last_client.send('Content-Type: {}{}'.format(content_type, enter_code))
        self.last_client.send('Connection: close{}{}'.format(enter_code, enter_code))
        self.last_client.sendall(content)
    
    def handleClient(self) -> None:
        try:
            client, addr = None, None
            client, addr = self.sock.accept()
            self.last_client = client
            client.settimeout(1)
            data = client.recv(512)
            end_idx = data.find(b' HTTP')
            if end_idx != -1:
                data = data[:end_idx]
                data = data.split(b" ")[-1]
                query = data.replace(b" ", b"").decode("utf-8")
                if query in self.handle_dict:
                    self.handle_dict[query]()
            else:
                pass
                
            client.close()
            gc.collect() 
        except Exception as e:
            if client:
                client.close()
            # print("Exception : ", e)


if __name__ == "__main__":
    def basic_test():
        print("wlan : ", wlan)
        print("get_ap_list : ", get_ap_list())
        print("get_wifi_list : ", get_wifi_list())
        print("isconnected : ", isconnected())
        print("get_connect_info : ", get_connect_info())
        print("get_ip : ", get_ip())
        print("get_subnet : ", get_subnet())
        print("get_gateway : ", get_gateway())
        print("get_dns : ", get_dns())
    
    def wifi_connect_test():
        # connect test
        ssid = ""
        password = ""

        print("disconnect : ", disconnect())
        print("connect : ", connect(ssid, password))
        print("isconnected : ", isconnected())
        print("status : ", "WL_CONNECTED" if status() == WL_CONNECTED else "WL_DISCONNECTED")
        print("get_connect_info : ", get_connect_info())
        print("get_ip : ", get_ip())
        print("get_subnet : ", get_subnet())
        print("get_gateway : ", get_gateway())
        print("get_dns : ", get_dns())
        print("get_mac : ", get_mac())
    
    def web_server_test():
        ssid = ""
        password = ""

        print("connect : ", connect(ssid, password))
        server = WebServer(80)
        server.on("/test", lambda: server.send(200, "text/plain", "hello from ET-board!"))
        server.begin()
        for x in range(50):
            server.handleClient()

        print("disconnect : ", disconnect())
        print("status : ", "WL_CONNECTED" if status() == WL_CONNECTED else "WL_DISCONNECTED")
        
    web_server_test()

# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr│
# │                                           │
# └───────────────────────────────────────────┘
