import socket
import network
import time
from car import forward,backward,turn,right,lighton,lightoff,stop
from html import web_page
from sn90 import trangle,udangle
import gc
import esp

esp.osdebug(None)
gc.collect()
wlan = network.WLAN(network.STA_IF)#創一個接口
wlan.active(True)#開啟網路
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('test','888888887777777')
    while not wlan.isconnected():
            pass
print("http://{}".format(wlan.ifconfig()[0]))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#伺服器跟伺服器對連用tcp協定雙向溝通
s.bind(('', 80))#可以跟sever任意連接
s.listen(5)
while True:
    conn, addr = s.accept()
    #conn是新socket,用來接收新資料,addr是連結用戶端ip位置,s=socket,accept是連結
    print("Got connection from %s" % str(addr))
    request = conn.recv(1024)
    #向客戶端發送1024字節
    request = str(request)
    forward1 = request.find('/?car=1')
    backward1 = request.find('/?car=2')
    stop1 = request.find('/?car=3')
    turn1 = request.find('/?car=4')
    right1 = request.find('/?car=5')
    lighton1 = request.find('/?light=6')
    lightoff1 = request.find('/?light=7')
    trangle1 = request.find('/?angle=8')
    udangle1 = request.find('/?angle=9')
    if forward1 == 6:
        print('前進')
        forward()
        time.sleep(1)
    elif backward1 == 6:
        print('後退')
        backward()
        time.sleep(1)
    elif stop1 == 6:
        print('停止')
        stop()
        time.sleep(1)
    elif turn1 == 6:
        print('左轉')
        turn()
        time.sleep(1)
    elif right1 == 6:
        print('右轉')
        right()
        time.sleep(1)
    elif lighton1 == 6:
        print('開燈')
        lighton()
        time.sleep(1)
    elif lightoff1 == 6:
        print('關燈')
        lightoff()
        time.sleep(1)
    elif trangle1 == 6:
        print('左右')
        trangle()
        time.sleep(1)
    elif udangle1 == 6:
        print('上下')
        udangle()
        time.sleep(1)
        
    response = web_page()
    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n")
        #建構http 
    conn.sendall(response)
    conn.close()