import Leds as led
import Legs as leg
import Sensor as sensor
import time
import LedMuster as ledmuster
import sys

#Startet alle sensoren
leg.init()
led.init()
sensor.init()

while True:
    try:
        #Wartet darauf, dass der Scanner etwas erkennt
        if sensor.IsDistanceLowerThen(150):
            #Startet ein zufälliges program
            ledmuster.callRandomPreset()
    except:
        sys.exit()
        pass
