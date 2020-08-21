from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time
import DeltaLaufRoboter as botti

for i in range(0,10):
    kit.servo[i].actuation_range = 120

while True:
    x = int(input("X: "))
    y = int(input("Y: "))
    z = int(input("Z: "))

    akk, bkk, ckk = botti.delta_calcInverse(x,y,z)

    akk=akk*-1+105
    bkk=bkk*-1+105
    ckk=ckk*-1+105

    kit.servo[0].angle = akk
    kit.servo[1].angle = bkk
    kit.servo[2].angle = ckk


    kit.servo[4].angle = akk
    kit.servo[5].angle = bkk
    kit.servo[6].angle = ckk

    kit.servo[8].angle = akk
    kit.servo[9].angle = bkk
    kit.servo[10].angle = ckk
