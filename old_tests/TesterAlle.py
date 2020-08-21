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

for i in range(16):
    kit.servo[i].actuation_range = 120
    kid.servo[i].actuation_range = 120
    
    
Arm = int(input("Welcher Arm soll angesteuert werden? Gib eine Zahl zwischen 1 und 6 ein."))

    
while True:

    if Arm == 1:
        a1 = int(input("Winkel a1: "))
        b1 = int(input("Winkel b1: "))
        c1 = int(input("Winkel c1: "))
        kit.servo[0].angle = a1
        kit.servo[1].angle = b1
        kit.servo[2].angle = c1
    elif Arm == 2:
        a2 = int(input("Winkel a2: "))
        b2 = int(input("Winkel b2: "))
        c2 = int(input("Winkel c2: "))
        kit.servo[4].angle = a2
        kit.servo[5].angle = b2
        kit.servo[6].angle = c2
    elif Arm == 3:
        a3 = int(input("Winkel a3: "))
        b3 = int(input("Winkel b3: "))
        c3 = int(input("Winkel c3: "))
        kit.servo[8].angle = a3
        kit.servo[9].angle = b3
        kit.servo[10].angle = c3
    elif Arm == 4:
        a4 = int(input("Winkel a4: "))
        b4 = int(input("Winkel b4: "))
        c4 = int(input("Winkel c4: "))
        kid.servo[0].angle = a4
        kid.servo[1].angle = b4
        kid.servo[2].angle = c4
    elif Arm == 5:
        a5 = int(input("Winkel a5: "))
        b5 = int(input("Winkel b5: "))
        c5 = int(input("Winkel c5: "))
        kid.servo[4].angle = a5
        kid.servo[5].angle = b5
        kid.servo[6].angle = c5
    elif Arm == 6:    
        a6 = int(input("Winkel a6: "))
        b6 = int(input("Winkel b6: "))
        c6 = int(input("Winkel c6: "))
        kid.servo[8].angle = a6
        kid.servo[9].angle = b6
        kid.servo[10].angle = c6