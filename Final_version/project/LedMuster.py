import Leds as led
import Legs as leg
import time
from operator import methodcaller as mCaller
import random

#Starts the modules
led.init()
leg.init()

'''
    Sucht eine Zufällige preset_ methode
'''
def callRandomPreset():
    # Holt sich alle Methoden welche in frage kommen
    methodes = list(filter(lambda x: "__" not in x,dir(Presets)))
    
    #Holt sich einen zufälligen methoden index
    x = random.randint(0,len(methodes)-1);
    
    #Gibt eine Zufällige methode Zurück
    return mCaller(methodes[x])(Presets)

#######################################################
## Preset methoden sollen immer mit preset_ beginnen ##
#######################################################

class Presets:
    
    def preset_1():
        for i in range(12):
            led.setForAllWheels(i, 255,0,0)
        for n in range(12):
            led.set(n+12,0,255,0)
            led.set(n,255,0,0)
        leg.move(leg.MAX,leg.MAX,leg.MAX,0,leg.G1)
        time.sleep(.7)
        for n in range(12):
            led.set(n+12,255,0,0)
            led.set(n+24,0,255,0)
        leg.move(leg.MIN,leg.MIN,leg.MIN,0,leg.G1)
        leg.move(leg.MAX,leg.MAX,leg.MAX,0,leg.G2)
        time.sleep(.7)
        for n in range(12):
            led.set(n+24,255,0,0)
            led.set(n+36,0,255,0)
        leg.move(leg.MIN,leg.MIN,leg.MIN,0,leg.G2)
        leg.move(leg.MAX,leg.MAX,leg.MAX,8,leg.G1)
        time.sleep(.7)
        for n in range(12):
            led.set(n+36,255,0,0)
            led.set(n+48,0,255,0)
        leg.move(leg.MIN,leg.MIN,leg.MIN,8,leg.G1)
        leg.move(leg.MAX,leg.MAX,leg.MAX,4,leg.G2)
        time.sleep(.7)
        for n in range(12):
            led.set(n+48,255,0,0)
            led.set(n+60,0,255,0)
        leg.move(leg.MIN,leg.MIN,leg.MIN,4,leg.G2)
        leg.move(leg.MAX,leg.MAX,leg.MAX,4,leg.G1)
        time.sleep(.7)
        for n in range(12):
            led.set(n+60,255,0,0)
            led.set(n,0,255,0)
        leg.move(leg.MIN,leg.MIN,leg.MIN,4,leg.G1)
        leg.move(leg.MAX,leg.MAX,leg.MAX,8,leg.G2)
        time.sleep(.7)
        for n in range(12):
            led.set(n+12,0,0,0)
            led.set(n+24,0,0,0)
            led.set(n+36,0,0,0)
            led.set(n+48,0,0,0)
            led.set(n+60,0,0,0)
            led.set(n,0,0,0)        
        leg.move(leg.MIN,leg.MIN,leg.MIN,8,leg.G2)
        for i in range(12):
            led.setForAllWheels(i, 0,0,0)
            
    def preset_2():
        for i in range(72):
            led.set(i,200,200,200)
        leg.move(leg.MAX,leg.MAX,leg.MAX,0,leg.G1)
        leg.move(leg.MAX,leg.MAX,leg.MAX,4,leg.G1)
        leg.move(leg.MAX,leg.MAX,leg.MAX,8,leg.G1)
        leg.move(leg.MAX,leg.MAX,leg.MAX,0,leg.G2)
        leg.move(leg.MAX,leg.MAX,leg.MAX,4,leg.G2)
        leg.move(leg.MAX,leg.MAX,leg.MAX,8,leg.G2)
        time.sleep(1)
        leg.move(leg.MIN,leg.MIN,leg.MIN,0,leg.G1)
        leg.move(leg.MIN,leg.MIN,leg.MIN,4,leg.G1)
        leg.move(leg.MIN,leg.MIN,leg.MIN,8,leg.G1)
        leg.move(leg.MIN,leg.MIN,leg.MIN,0,leg.G2)
        leg.move(leg.MIN,leg.MIN,leg.MIN,4,leg.G2)
        leg.move(leg.MIN,leg.MIN,leg.MIN,8,leg.G2)
        for i in range(72):
            led.set(i,0,0,0)
            
    def preset_3():
        for i in range(72):
            led.set(i,0,0,255)
        leg.moveAll(leg.MIN,leg.MIN,leg.MAX)
        time.sleep(1)
        for i in range(72):
            led.set(i,0,255,0)
        leg.moveAll(leg.MIN,leg.MAX,leg.MIN)
        time.sleep(1)
        for i in range(72):
            led.set(i,255,0,0)
        leg.moveAll(leg.MAX,leg.MIN,leg.MIN)
        time.sleep(1)
        leg.moveAll(leg.MIN,leg.MIN,leg.MIN)
        for i in range(72):
            led.set(i,0,0,0)
            
    def preset_4():
        for x in range(5):
            for i in range(12):
                led.setForAllWheels(i,200,0,0)
                time.sleep(.005)
            for i in range(12):
                led.setForAllWheels(i,0,200,0)
                time.sleep(.005)
            for i in range(12):
                led.setForAllWheels(i,0,0,200)
                time.sleep(.005)
            for i in range(12):
                led.setForAllWheels(i,0,0,0)
