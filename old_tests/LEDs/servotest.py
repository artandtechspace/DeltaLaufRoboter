from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x40)
kid = ServoKit(channels=16, address=0x60)

import threading
import time

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
    
initRotor(0,kit)
initRotor(4,kit)
initRotor(8,kit)

initRotor(0,kid)
initRotor(4,kid)
initRotor(8,kid)

while True:
    #Moves kit one
    move(max,max,min,0,kit)
    move(max,max,min,4,kit)
    move(max,max,min,8,kit)
    
    move(min,min,min,0,kid)
    move(max,max,max,4,kid)
    move(min,min,min,8,kid)
    
    time.sleep(.5)
    
    move(max,min,max,0,kit)
    move(max,min,max,4,kit)
    move(max,min,max,8,kit)
    
    move(max,max,max,0,kid)
    move(min,min,min,4,kid)
    move(max,max,max,8,kid)
    
    time.sleep(.5)
    
    move(min,max,max,0,kit)
    move(min,max,max,4,kit)
    move(min,max,max,8,kit)
    
    time.sleep(.5)
    
    