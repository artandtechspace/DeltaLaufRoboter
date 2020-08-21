from evdev import list_devices, InputDevice, categorize, ecodes

import Coordutil
from adafruit_servokit import ServoKit
groupA = ServoKit(channels=16,address=0x40)
groupB = ServoKit(channels=16,address=0x60)
import time 
import DeltaLaufRoboter as botti
import threading
import numpy

for i in range(16):
    groupA.servo[i].actuation_range = 120
    groupB.servo[i].actuation_range = 120 
                
def moveB(x,y,z):
   # print("{} {}".format(x,y))
    x,y,z = Coordutil.portCoords(x,y,z)
    x,y = Coordutil.addDegrees(x,y,160)
    botXB,botYB,botZB = botti.delta_calcInverse(x,y,z)
    try:
        groupB.servo[0].angle = -2*botXB+22 #Motor D
        groupB.servo[1].angle = -2*botYB+27 #Motor E
        groupB.servo[2].angle = -2*botZB+25 #Motor F
        
        groupB.servo[4].angle = -2*botXB+27
        groupB.servo[5].angle = -2*botYB+40
        groupB.servo[6].angle = -2*botZB+25
        
        groupB.servo[8].angle = -2*botXB+23
        groupB.servo[9].angle = -2*botYB+26
        groupB.servo[10].angle = -2*botZB+25
    except:
        print("Runtime Error")
    
def moveA(x,y,z):
    x,y,z = Coordutil.portCoords(x,y,z)
    #x,y = Coordutil.addDegrees(x,y,60)
    botX,botY,botZ = botti.delta_calcInverse(x,y,z)
    try:
        groupA.servo[0].angle = -2*botX+35 #Motor A
        groupA.servo[1].angle = -2*botY+39 #Motor B
        groupA.servo[2].angle = -2*botZ+33 #Motor C
        
        groupA.servo[4].angle = -2*botX+35
        groupA.servo[5].angle = -2*botY+23
        groupA.servo[6].angle = -2*botZ+33
        
        groupA.servo[8].angle = -2*botX+27
        groupA.servo[9].angle = -2*botY+27
        groupA.servo[10].angle = -2*botZ+35
    except:
        pass
        #print("Runtime Error")


while True:
    time.sleep(1)
    moveA(0,0,-50)
    moveB(0,0,-100)
    time.sleep(1)
    while True:
        for i in range(50):
            moveA(i,0,-50)
            time.sleep(0.01)
            
        for i in range(50):
            moveA(50,0,-i-50)
            time.sleep(0.01)
            
        for i in range(100):
            moveA(50-i,0,-100)
            time.sleep(0.01)
            
        for i in range(50):
            moveA(-50,0,-100+i)
            time.sleep(0.01)
            
        for i in range(50):
            moveA(-50+i,0,-50)
            time.sleep(0.01)
    
    """
    #Walking Lasse
    while True:
        moveA(0,0,0)
        moveB(0,0,100)
        sleep(1)
        
        moveA(90,0,0)
        moveB(0,-90,100)
        sleep(1)
        
        moveA(90,0,100)
        moveB(0,-90,0)
        sleep(1)
        
        moveA(-90,0,100)
        moveB(0,90,0)
        sleep(1)
        
        moveA(-90,0,0)
        moveB(0,90,100)
        sleep(1)
        
        print("Restart")
    """
    """
    while True:
        moveA(100,0,0)
        sleep(1)
        moveA(100,0,100)
        sleep(1)
        moveB(0,0,0)
        sleep(1)
        moveA(-100,0,100)
        sleep(1)
        moveB(100,0,100)
        sleep(1)
        moveA(0,0,0)
        sleep(1)
        moveB(-100,0,100)
        sleep(1)
        print("Restart")
        """
