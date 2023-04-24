from machine import Pin
from machine import PWM
light = Pin(2,Pin.OUT)

global n
n=10
pin1 = PWM(Pin(4,Pin.OUT))
pin1.freq(n)
pin2 = PWM(Pin(14,Pin.OUT))
pin2.freq(n)
pin3 = PWM(Pin(33,Pin.OUT))
pin3.freq(n)
pin4 = PWM(Pin(32,Pin.OUT))
pin4.freq(n)

def forward():
    pin1.duty(400)
    pin2.duty(0)
    pin3.duty(400)
    pin4.duty(0)

def backward():
    pin1.duty(0)
    pin2.duty(400)
    pin3.duty(0)
    pin4.duty(400)

def stop():
    pin1.duty(0)
    pin2.duty(0)
    pin3.duty(0)
    pin4.duty(0)

def turn():
    pin1.duty(0)
    pin2.duty(0)
    pin3.duty(400)
    pin4.duty(0)
    
def right():
    pin1.duty(400)
    pin2.duty(0)
    pin3.duty(0)
    pin4.duty(0)
    
def lighton():
    light.on()

def lightoff():
    light.off()
    
def faston():
    global n 
    n+=10
    if n<100:
        print(n)
        return n
    else:
        n=100
        print(n)
        return n
def fastoff():
    global n
    n-=10
    if n>10:
        print(n)
        return n
    else:
        n=10
        print(n)
        return n