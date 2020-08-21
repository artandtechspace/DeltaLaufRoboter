from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x40)
kid = ServoKit(channels=16, address=0x60)

import threading
import time
import RPi.GPIO as GPIO

min = 40
max = 120

def initRotor(rotor,F):
    F.servo[rotor].actuation_range = 120  #Set actuation range of Servo 0 to 120
    F.servo[rotor+1].actuation_range = 120  #Set actuation range of Servo 2 to 120
    F.servo[rotor+2].actuation_range = 120  #Set actuation range of Servo 2 to 120

def move(α,β,γ,rotor,F):
    F.servo[rotor].angle = α
    F.servo[rotor+1].angle = β
    F.servo[rotor+2].angle = γ



GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 13
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distanz():
    GPIO.output(GPIO_TRIGGER, True)
    
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    StartZeit = time.time()
    StopZeit = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()
        
    TimeElapsed = StopZeit - StartZeit
    
    distanz = (TimeElapsed * 34300 / 2)
    return distanz
def mappen(vari, fromlow, fromhigh, tolow, tohigh):
    wert = ((vari-fromlow)/(fromhigh-fromlow)*(tohigh-tolow))+tolow
    if wert < tolow:
        wert = tolow
    elif wert > tohigh:
        wert = tohigh
    return wert

initRotor(0,kit)

while True:
    print(mappen(50,25,75,100,200))
    winkel = mappen(distanz(),15,100,min,max )
    print(winkel)
    #print(distanz())
    move(winkel, winkel, winkel, 0, kit)
    move(winkel, winkel, winkel, 4, kit)
    move(winkel, winkel, winkel, 8, kit)    