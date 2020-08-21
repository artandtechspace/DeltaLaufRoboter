import RPi.GPIO as GPIO
import time
import sys

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
    
    distanz = (TimeElapsed * 34200 / 2)
    return distanz

while True:
    try:
        abstand = distanz()
        print("Gemessene Entfernung = %.1f cm" % abstand)
        time.sleep(1)
    except KeyboardInterrupt:
        print("Messung von User gestoppt")
        GPIO.cleanup()
        sys.exit()
        
        