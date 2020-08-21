import board
import neopixel
import random

pixels = neopixel.NeoPixel(board.D18,72)

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x40)
kid = ServoKit(channels=16, address=0x60)

import threading
import time
import RPi.GPIO as GPIO

min = 40
max = 120


def sameforall(led, red, green, blue):
    pixels[led]    = (red, green, blue)
    pixels[led+12] = (red, green, blue)
    pixels[led+24] = (red, green, blue)
    pixels[led+36] = (red, green, blue)
    pixels[led+48] = (red, green, blue)

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

def lessthan(distance, loops = 5):
    summe =0
    for i in range(loops):
        summe += distanz()
    if summe/5 <= distance:
        return True
    elif summe/5 > distance:
        return False
    
initRotor(0,kit)
move(min,min,min,0,kit)
move(min,min,min,4,kit)
move(min,min,min,8,kit)
    
move(min,min,min,0,kid)
move(min,min,min,4,kid)
move(min,min,min,8,kid)

def AllServos(α2,β2,γ2):
    move(α2,β2,γ2,0,kit)
    move(α2,β2,γ2,4,kit)
    move(α2,β2,γ2,8,kit)
    move(α2,β2,γ2,0,kid)
    move(α2,β2,γ2,4,kid)
    move(α2,β2,γ2,8,kid)
def Muster1():
    for i in range(12):
        sameforall(i, 255,0,0)
    for n in range(12):
        pixels[n+12] = (0,255,0)
        pixels[n]    = (255,0,0)
    move(max,max,max,0,kit)
    time.sleep(.7)
    for n in range(12):
        pixels[n+12] = (255,0,0)
        pixels[n+24] = (0,255,0)
    move(min,min,min,0,kit)
    move(max,max,max,0,kid)
    time.sleep(.7)
    for n in range(12):
        pixels[n+24] = (255,0,0)
        pixels[n+36] = (0,255,0)
    move(min,min,min,0,kid)
    move(max,max,max,8,kit)
    time.sleep(.7)
    for n in range(12):
        pixels[n+36] = (255,0,0)
        pixels[n+48] = (0,255,0)
    move(min,min,min,8,kit)
    move(max,max,max,4,kid)
    time.sleep(.7)
    for n in range(12):
        pixels[n+48] = (255,0,0)
        pixels[n+60] = (0,255,0)
    move(min,min,min,4,kid)
    move(max,max,max,4,kit)
    time.sleep(.7)
    for n in range(12):
        pixels[n+60] = (255,0,0)
        pixels[n]    = (0,255,0)
    move(min,min,min,4,kit)
    move(max,max,max,8,kid)
    time.sleep(.7)
    for n in range(12):
        pixels[n+12] = (0,0,0)
        pixels[n+24] = (0,0,0)
        pixels[n+36] = (0,0,0)
        pixels[n+48] = (0,0,0)
        pixels[n+60] = (0,0,0)
        pixels[n]    = (0,0,0)        
    move(min,min,min,8,kid)
    for i in range(12):
        sameforall(i, 0,0,0)
def Muster2():
    for i in range(72):
        pixels[i] = (200,200,200)
    move(max,max,max,0,kit)
    move(max,max,max,4,kit)
    move(max,max,max,8,kit)
    move(max,max,max,0,kid)
    move(max,max,max,4,kid)
    move(max,max,max,8,kid)
    time.sleep(1)
    move(min,min,min,0,kit)
    move(min,min,min,4,kit)
    move(min,min,min,8,kit)
    move(min,min,min,0,kid)
    move(min,min,min,4,kid)
    move(min,min,min,8,kid)
    for i in range(72):
        pixels[i] = (0,0,0)
def Muster3():
    for i in range(72):
        pixels[i] = (0,0,255)
    AllServos(min,min,max)
    time.sleep(1)
    for i in range(72):
        pixels[i] = (0,255,0)
    AllServos(min,max,min)
    time.sleep(1)
    for i in range(72):
        pixels[i] = (255,0,0)
    AllServos(max,min,min)
    time.sleep(1)
    AllServos(min,min,min)
    for i in range(72):
        pixels[i] = (0,0,0)
def Muster4():
    for x in range(5):
        for i in range(12):
            sameforall(i,200,0,0)
            time.sleep(.005)
        for i in range(12):
            sameforall(i,0,200,0)
            time.sleep(.005)
        for i in range(12):
            sameforall(i,0,0,200)
            time.sleep(.005)
        for i in range(12):
            sameforall(i,0,0,0)

while True:
    if lessthan(50):
        zufall = random.randint(0,3)
        if zufall == 0:
            Muster1()
        if zufall == 1:
            Muster2()
        if zufall == 2:
            Muster3()
        if zufall == 3:
            Muster4()
        