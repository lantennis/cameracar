from machine import PWM
from machine import Pin

pin12 = PWM(Pin(12))
pin12.freq(50)
pin12.duty_u16(1638)

pin13 = PWM(Pin(13))
pin13.freq(50)
pin13.duty_u16(1638)


duty_num = 1638
def trunsg90():
    global duty_num
    if duty_num<8192:
        duty_num+=500
        pin12.duty_u16(duty_num)
        print("0")
    else:
        duty_num =8192
        print("0")
def rightsg90():
    global duty_num
    if duty_num>1638:
        duty_num-=500
        pin12.duty_u16(duty_num)
        print("1")
    else:
        duty_num = 1638
        print("1")
            
def upsg90():
    global duty_num
    if duty_num<8192:
        duty_num+=500
        pin13.duty_u16(duty_num)
        print("0")
    else:
        duty_num =8192
        print("0")
        
def downsg90():
    global duty_num
    if duty_num>1638:
        duty_num-=500
        pin13.duty_u16(duty_num)
        print("1")
    else:
        duty_num = 1638
        print("1")