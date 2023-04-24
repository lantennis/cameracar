import socket
import network
import camera
import time
from machine import Pin

light=Pin(4,Pin.OUT)
wlan = network.WLAN(network.STA_IF)#創一個接口
wlan.active(True)#開啟網路
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('test','888888887777777')
    while not wlan.isconnected():
        pass
print("http://{}".format(wlan.ifconfig()[0]))

try:
    camera.init(0, format=camera.JPEG)  # 鏡頭初始化
except Exception as e:
    camera.deinit()#釋放相機所占資源
    camera.init(0, format=camera.JPEG)

light.on()
time.sleep(1)
light.off()
camera.flip(0)  # 上翻下翻
camera.mirror(1)  # 左右
camera.framesize(camera.FRAME_QVGA)  # 分辨率(預設)
camera.speffect(camera.EFFECT_NONE)  # 無特效
camera.whitebalance(camera.WB_NONE)  # 白平衡
camera.saturation(2)  # 飽和度
camera.brightness(0)  # 亮度
camera.contrast(2)  # 對比度
camera.quality(10)  # 質量(最高)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#伺服器跟伺服器對連用tcp協定雙向溝通
s.bind(('', 80))#可以跟sever任意連接
s.listen(5)#最多5人連接

while True:
    conn, addr = s.accept()
        #conn是新socket,用來接收新資料,addr是連結用戶端ip位置,s=socket,accept是連結
    request = conn.recv(1024)
        #向客戶端發送1024字節
    response = "HTTP/1.0 200 OK\r\nContent-Type: multipart/x-mixed-replace; boundary=frame\r\n\r\n"
        #建構http
    conn.send(response)

    while True:
        try:
            buf = camera.capture()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send("--frame\r\n")#發送視頻數據
            conn.send("Content-Type: image/jpeg\r\n")#發送Jpeg圖片
            conn.send("Content-Length: %d\r\n\r\n" % len(buf))#表示要發送的東西
            conn.sendall(buf)#發送數據直到發送完成或關閉,有問題可以發送錯誤
            time.sleep(0.1)
        except Exception as e:#錯誤容納值
            break
conn.close()