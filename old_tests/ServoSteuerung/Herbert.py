from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x40)
kid = ServoKit(channels=16, address=0x60)
import time
import DeltaLaufRoboter as botti
penis = -1.166

from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 40

for i in range(16):
    kit.servo[i].actuation_range = 120
    kid.servo[i].actuation_range = 120 

botti.ParabelAll(40, 40, -125,0.02)
for i in range (200,-200,-1):
    t1, t2, t3 = botti.delta_calcInverse(i/10,i/10,-125)
    u1, u2, u3 = botti.delta_calcInverse(i/-10,i/-10,-125)
    kit.servo[0].angle = t1*penis+105
    kit.servo[1].angle = t2*penis+105
    kit.servo[2].angle = t3*penis+105
    kit.servo[4].angle = t1*penis+105
    kit.servo[5].angle = t2*penis+105
    kit.servo[6].angle = t3*penis+105
    kit.servo[8].angle = t1*penis+105
    kit.servo[9].angle = t2*penis+105
    kit.servo[10].angle= t3*penis+105
            
    kid.servo[0].angle = u1*penis+105
    kid.servo[1].angle = u2*penis+105
    kid.servo[2].angle = u3*penis+105
    kid.servo[4].angle = u1*penis+105
    kid.servo[5].angle = u2*penis+105
    kid.servo[6].angle = u3*penis+105
    kid.servo[8].angle = u1*penis+105
    kid.servo[9].angle = u2*penis+105
    kid.servo[10].angle= u3*penis+105
    #time.sleep(0.001)
botti.ParabelInvAll(-40, -40, -125, 0.02)

    
