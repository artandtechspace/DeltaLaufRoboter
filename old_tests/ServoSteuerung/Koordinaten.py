from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time
import DeltaLaufRoboter as botti

kit.servo[0].actuation_range = 120 
kit.servo[1].actuation_range = 120  
kit.servo[2].actuation_range = 120


while True:
    '''
    x = int(input("X: "))
    y = int(input("Y: "))
    z = int(input("Z: "))
    
    akk, bkk, ckk = botti.delta_calcInverse(x,y,z)
    
    kit.servo[0].angle = akk*-1+105
    kit.servo[1].angle = bkk*-1+105
    kit.servo[2].angle = ckk*-1+105  
    
    
    kit.servo[4].angle = akk*-1+105
    kit.servo[5].angle = bkk*-1+105
    kit.servo[6].angle = ckk*-1+105
    
    kit.servo[8].angle = akk*-1+105
    kit.servo[9].angle = bkk*-1+105
    kit.servo[10].angle = ckk*-1+105
    '''

    kit.servo[0].angle = 75
    kit.servo[1].angle = 75
    kit.servo[2].angle = 75
    
    kit.servo[4].angle = 75
    kit.servo[5].angle = 75
    kit.servo[6].angle = 75
    
    kit.servo[8].angle = 75
    kit.servo[9].angle = 75
    kit.servo[10].angle = 75
    print(75)
    time.sleep(1)
    kit.servo[0].angle = 105
    kit.servo[1].angle = 105
    kit.servo[2].angle = 105  
   
    kit.servo[4].angle = 105
    kit.servo[5].angle = 105
    kit.servo[6].angle = 105  
    
    kit.servo[8].angle = 105
    kit.servo[9].angle = 105
    kit.servo[10].angle = 105
    print(105)
    time.sleep(1)