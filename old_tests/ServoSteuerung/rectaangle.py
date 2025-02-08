from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x40)
kid = ServoKit(channels=16, address=0x60)
import time
import DeltaLaufRoboter as botti
penis = -1.166
a = 50

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

#botti.ParabelAll(20, 20, -125,0.02)
#t1, t2, t3 = botti.delta_calcInverse(20,0,-125)
#botti.move_all_a(t1*penis+105,t2*penis+105,t3*penis+105)
while True:

    for i in range (a,-a,-1):
        botti.moveInv_all(i,a,-125)
    for i in range (a,-a,-1):
        botti.moveInv_all(-a,i,-125)
    for i in range (-a,a,1):
        botti.moveInv_all(i,-a,-125)
    for i in range (-a,a,1):
        botti.moveInv_all(a,i,-125)