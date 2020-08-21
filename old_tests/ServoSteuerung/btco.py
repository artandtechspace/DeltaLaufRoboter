from evdev import InputDevice, categorize, ecodes
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

import DeltaLaufRoboter as botti

kit.servo[0].actuation_range = 120 
kit.servo[1].actuation_range = 120  
kit.servo[2].actuation_range = 120

gamepad = InputDevice('/dev/input/event6')

x=1
y=-300
z=1

def handleHeight(value):
    z= 80*(value/255)-318

def handleX(value):
    x=300*(value/255)-150

def handleY(value):
    y=300*(value/255)-150

for event in gamepad.read_loop():
    if event.code == 1:
        handleHeight(event.value)
        print("X:{} Y:{} Z:{}".format(x,y,z));
        t1, t2, t3 = botti.delta_calcInverse(x,y,z)
        kit.servo[0].angle = t1*-1+107
        kit.servo[1].angle = t2*-1+105
        kit.servo[2].angle = t3*-1+102
    elif event.code == 16:
        handleX(event.value)
        print("X:{} Y:{} Z:{}".format(x,y,z));
        t1, t2, t3 = botti.delta_calcInverse(x,y,z)
        kit.servo[0].angle = t1*-1+107
        kit.servo[1].angle = t2*-1+105
        kit.servo[2].angle = t3*-1+102
    elif event.code == 17:
        handleY(event.value)
        print("X:{} Y:{} Z:{}".format(x,y,z));
        t1, t2, t3 = botti.delta_calcInverse(x,y,z)
        kit.servo[0].angle = t1*-1+107
        kit.servo[1].angle = t2*-1+105
        kit.servo[2].angle = t3*-1+102
    elif event.code != 0 and event.code != 3:
        print(event)
 

'''
1:
    X O [] /_\
    
    Schultertasten
    
    Knueppel rein
    
    Options/Share
    
    Ps Taste
    
3:
    Steuerknuepel
    
    Kreuz

'''