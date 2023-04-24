from machine import Pin
from matchine import PWM

light = Pin(2,Pin.OUT)
pin1 = PWM(Pin(4,Pin.OUT),freq=10)
pin2 = PWM(Pin(14,Pin.OUT),freq=10)
pin3 = PWM(Pin(26,Pin.OUT),freq=10)
pin4 = PWM(Pin(27,Pin.OUT),freq=10)


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
    pin1.duty(400)
    pin2.duty(0)
    pin3.duty(0)
    pin4.duty(0)
    
def right():
    pin1.duty(0)
    pin2.duty(0)
    pin3.duty(400)
    pin4.off()
    
def lighton():
    light.on()

def lightoff():
    light.off()
