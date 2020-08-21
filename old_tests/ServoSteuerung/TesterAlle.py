from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x40)
kid = ServoKit(channels=16, address=0x60)

import time
import DeltaLaufRoboter as botti

from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 40hz.
pca.frequency = 40
StartPunkt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
StardPunkt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    kit.servo[i].actuation_range = 120
    kid.servo[i].actuation_range = 120
for i in range(10):
    print("A:" + str(StartPunkt[i] ))
    print("B:" + str(StardPunkt[i] ))
    print(str(i))
    
    kit.servo[i].angle = StartPunkt[i]+30 
    kid.servo[i].angle = StardPunkt[i] +30

    
Arm = int(input("Welcher Arm soll angesteuert werden? Gib eine Zahl zwischen 1 und 6 ein."))

    
while True:

    if Arm == 1:
        a1 = int(input("Winkel a1: "))
        b1 = int(input("Winkel b1: "))
        c1 = int(input("Winkel c1: "))
        kit.servo[0].angle = 2*a1 +30
        kit.servo[1].angle = 2*b1 +30
        kit.servo[2].angle = 2*c1 +30
    elif Arm == 2:
        a2 = int(input("Winkel a2: "))
        b2 = int(input("Winkel b2: "))
        c2 = int(input("Winkel c2: "))
        kit.servo[4].angle = 2*a2 +30
        kit.servo[5].angle = 2*b2 +30
        kit.servo[6].angle = 2*c2 +30
    elif Arm == 3:
        a3 = int(input("Winkel a3: "))
        b3 = int(input("Winkel b3: "))
        c3 = int(input("Winkel c3: "))
        kit.servo[8].angle = 2*a3 +30
        kit.servo[9].angle = 2*b3 +30
        kit.servo[10].angle = 2*c3 +30
    elif Arm == 4:
        a4 = int(input("Winkel a4: "))
        b4 = int(input("Winkel b4: "))
        c4 = int(input("Winkel c4: "))
        kid.servo[0].angle = 2*a4 +30
        kid.servo[1].angle = 2*b4 +30
        kid.servo[2].angle = 2*c4 +30
    elif Arm == 5:
        a5 = int(input("Winkel a5: "))
        b5 = int(input("Winkel b5: "))
        c5 = int(input("Winkel c5: "))
        kid.servo[4].angle = 2*a5 +30
        kid.servo[5].angle = 2*b5 +30
        kid.servo[6].angle = 2*c5 +30
    elif Arm == 6:    
        a6 = int(input("Winkel a6: "))        
        b6 = int(input("Winkel b6: "))
        c6 = int(input("Winkel c6: "))
        kid.servo[8].angle = 2*a6 +30
        kid.servo[9].angle = 2*b6 +30
        kid.servo[10].angle = 2*c6 +30