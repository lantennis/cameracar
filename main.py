import socket
import network
import time
from car import forward,backward,turn,right,lighton,lightoff,stop,faston,fastoff
from html import web_page
from sn90 import trunsg90,rightsg90,upsg90,downsg90
import gc
import esp
from machine import Pin

light=Pin(2,Pin.OUT)
light.on()
time.sleep(1)
light.off()
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
    trunsg901 = request.find('/?angle=8')
    rightsg901 = request.find('/?angle=9')
    upsg901 = request.find('/?angle=10')
    downsg901 = request.find('/?angle=11')
    faston1 = request.find('/?fast=12')
    fastoff1 = request.find('/?fast=13')
    if forward1 == 6:
        print('前進')
        forward()
        
    elif backward1 == 6:
        print('後退')
        backward()
        
    elif stop1 == 6:
        print('停止')
        stop()
        
    elif turn1 == 6:
        print('左轉')
        turn()
        
    elif right1 == 6:
        print('右轉')
        right()

    elif lighton1 == 6:
        print('開燈')
        lighton()
        
    elif lightoff1 == 6:
        print('關燈')
        lightoff()
        
    elif trunsg901 == 6:
        print('左')
        trunsg90()
        
    elif rightsg901 == 6:
        print('右')
        rightsg90()
        
    elif upsg901 == 6:
        print('下')
        upsg90()
        
    elif downsg901 == 6:
        print('上')
        downsg90()
        
    elif faston1 == 6:
        print('速度上升')
        faston()
        
    elif fastoff1 == 6:
        print('速度下降')
        fastoff()
        
        
    response = web_page()
    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n")
        #建構http 
    conn.sendall(response)
    conn.close() 