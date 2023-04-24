from machine import PWM
from machine import Pin

pin12 = PWM(Pin(12))
pin12.freq(50)
pin12.duty_u16(1638)

pin13 = PWM(Pin(13))
pin13.freq(50)
pin13.duty_u16(1638)


duty_num = 1638
freq = 0
def trangle():
    global freq, duty_num
    if freq==0:
        if duty_num<8192:
            duty_num+=1638
            pin12.duty_u16(duty_num)
            print("0")
        else:
            duty_num =8192
            freq=1
        
    else:
        if duty_num>1638:
            duty_num-=1638
            pin12.duty_u16(duty_num)
            print("1")
        else:
            duty_num = 1638
            freq=0
            
def udangle():
    global freq, duty_num
    if freq==0:
        if duty_num<8192:
            duty_num+=1638
            pin13.duty_u16(duty_num)
            print("0")
        else:
            duty_num =8192
            freq=1
        
    else:
        if duty_num>1638:
            duty_num-=1638
            pin13.duty_u16(duty_num)
            print("1")
        else:
            duty_num = 1638
            freq=0