from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time
import DeltaLaufRoboter as botti

kit.servo[0].actuation_range = 120 
kit.servo[1].actuation_range = 120  
kit.servo[2].actuation_range = 120

kit.servo[4].actuation_range = 120 
kit.servo[5].actuation_range = 120  
kit.servo[6].actuation_range = 120

kit.servo[8].actuation_range = 120 
kit.servo[9].actuation_range = 120  
kit.servo[10].actuation_range = 120


while True:

    akk = int(input("Winkel a: "))
    bkk = int(input("Winkel b: "))
    ckk = int(input("Winkel c: "))
            
    kit.servo[0].angle = akk*-1+105
    kit.servo[1].angle = bkk*-1+105
    kit.servo[2].angle = ckk*-1+105
    
    kit.servo[4].angle = akk*-1+105
    kit.servo[5].angle = bkk*-1+105
    kit.servo[6].angle = ckk*-1+105
    
    kit.servo[8].angle = akk*-1+105
    kit.servo[9].angle = bkk*-1+105
    kit.servo[10].angle = ckk*-1+105
