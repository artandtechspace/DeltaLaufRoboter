import random
import RPi.GPIO as GPIO
import time

#Ob das Modul bereits gestartet wurde
isInited = False

'''
    Startet das Module
    @param triggerPin der Sensor-trigger-pin. Default = 13
    @param echoPin der Sensor-echo-pin. Default = 24
'''
def init(triggerPin = 13,echoPin = 24):
    global isInited
    if not isInited:
        isInited=True
        GPIO.setmode(GPIO.BCM)

        global GPIO_TRIGGER
        global GPIO_ECHO

        GPIO_TRIGGER = triggerPin
        GPIO_ECHO = echoPin

        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

'''
    Gibt die Distanze zurück, welche der Sensor gemessen hat.
'''
def _getDistance():
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

'''
    Gibt an ob die Distanze welche vom Scanner erfasst wird kleiner ist als der angegebene Wert
'''
def IsDistanceLowerThen(distance, loops = 5):
    summe =0
    for i in range(loops):
        summe += _getDistance()
    if summe/5 <= distance:
        return True
    elif summe/5 > distance:
        return False