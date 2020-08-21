from evdev import list_devices, InputDevice, categorize, ecodes

import Coordutil
from time import sleep
import DeltaLaufRoboter as botti

speed = 1
time = .02

class Group:
    def __init__(self,x,y,z,set):
        self.x = x
        self.y = y
        self.z = z
        self.set = set
        
    def move(self,x,y,z):
        global time
        global speed
        while self.x != x or self.y != y or self.z != z:
            mX=0
            mY=0
            mZ=0
            if self.x != x:
                if self.x<x:
                    mX = speed
                else:
                    mX = -speed
            if self.y != y:
                if self.y<y:
                    mY = speed
                else:
                    mY = -speed
            if self.z != z:
                if self.z<z:
                    mZ = speed
                else:
                    mZ = -speed
            self.x+=mX
            self.y+=mY
            self.z+=mZ
            self.set(self.x,self.y,self.z)
            sleep(time)
      
gA = Group(0,0,100,botti.moveA)
gB = Group(0,0,100,botti.moveB)

#Null position
gA.move(0,0,100)
gB.move(0,0,0)
"""
#Walking Lasse
while True:
    gA.move(0,0,0)
    gB.move(0,0,0)
    
    gA.move(40,0,0)
    gB.move(0,40,0)
    
    gA.move(40,0,0)
    gB.move(0,40,0)
    
    gA.move(-40,0,0)
    gB.move(0,-40,0)
    
    gA.move(-40,0,0)
    gB.move(0,-40,0)
"""
"""
#Walking
while True:
    #A Up
    gA.move(0,0,0)
    
    #B walk
    gB.move(0,50,100)
    
    #A forward
    gA.move(50,50,100)
    
    #B up
    gB.move(0,0,0)
    
    #A walk
    gA.move(-50,-50,100)
    
    #B forward
    gB.move(0,-50,100)
"""

'''
mA(0,0,100)
mA(-50,-50,100)
mA(50,50,100)
mA(-50,-50,100)
'''

'''
while True:
    moveA(50,50,100)
    moveB(0,0,0)
    sleep(0.25)
    moveA(30,30,100)
    sleep(0.25)
    moveA(10,10,100)
    sleep(0.25)
    moveA(-10,-10,100)
    sleep(0.25)
    moveA(-30,-30,100)
    sleep(0.25)
    moveA(-50,-50,100)
    sleep(0.25)
    moveB(20,20,20)
    sleep(0.25)
    moveB(40,40,40)
    sleep(0.25)
    moveB(50,50,60)
    sleep(0.25)
    moveB(50,50,80)
    sleep(0.25)
    moveB(50,50,100)
    sleep(0.25)
    moveA(-40,-40,80)
    sleep(0.25)
    moveA(-20,-20,60)
    sleep(0.25)
    moveA(0,0,40)
    sleep(0.25)
    moveA(0,0,20)
    sleep(0.25)
    moveA(0,0,0)
    sleep(0.25)
    moveB(30,30,100)
    sleep(0.25)
    moveB(10,10,100)
    sleep(0.25)
    moveB(-10,-10,100)
    sleep(0.25)
    moveB(-30,-30,100)
    sleep(0.25)
    moveB(-50,-50,100)
    sleep(0.25)
    moveA(20,20,20)
    sleep(0.25)
    moveA(40,40,40)
    sleep(0.25)
    moveA(50,50,60)
    sleep(0.25)
    moveA(50,50,80)
    sleep(0.25)
    moveA(50,50,100)
    sleep(0.25)
    moveB(-40,-40,80)
    sleep(0.25)
    moveB(-20,-20,60)
    sleep(0.25)
    moveB(0,0,40)
    sleep(0.25)
    moveB(0,0,20)
    sleep(0.25)
    moveB(0,0,0)
    '''