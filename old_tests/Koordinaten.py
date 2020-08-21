from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time
import DeltaLaufRoboter as botti

kit.servo[0].actuation_range = 120 
kit.servo[1].actuation_range = 120  
kit.servo[2].actuation_range = 120


while True:

    x = int(input("X: "))
    y = int(input("Y: "))
    z = int(input("Z: "))
    
    akk, bkk, ckk = botti.delta_calcInverse(x,y,z)
    
    kit.servo[0].angle = akk*-1+105
    kit.servo[1].angle = bkk*-1+105
    kit.servo[2].angle = ckk*-1+105
