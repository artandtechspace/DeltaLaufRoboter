from evdev import InputDevice, categorize, ecodes
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

import DeltaLaufRoboter as botti
Hohe = -265

kit.servo[0].actuation_range = 120 
kit.servo[1].actuation_range = 120  
kit.servo[2].actuation_range = 120

gamepad = InputDevice('/dev/input/event6')

for event in gamepad.read_loop():

    

#    if event.code!= 0 and event.code >= 300:
#      print(event)

    if event.code == 312:
        if event.code == 312 and Hohe >= -305:
            Hohe = Hohe -1
            print(Hohe)
        elif event.code == 313 and Hohe <= -255:
            Hohe = Hohe+1
            print(Hohe)
            '''
        if Hohe >= -255 and event.value != 0:
            Hohe = -1*(255 + event.value/5)
            if Hohe >= 0:
                Hohe = Hohe*-1
            print(Hohe)
            '''
            t1, t2, t3 = botti.delta_calcInverse(0,0,Hohe)
            kit.servo[0].angle = t1*-1+105
            kit.servo[1].angle = t2*-1+105
            kit.servo[2].angle = t3*-1+105
        else:
            print(event.value)
            Hohe = -255