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
    kit.servo[i].actuation_range = 180
    kid.servo[i].actuation_range = 180 

#botti.ParabelAll(20, 20, -125,0.02)
while True:
    for i in range (80,-80,-1):
        t1, t2, t3 = botti.delta_calcInverse(i/4,20,-125)
        botti.move_all_a(t1*penis+105,t2*penis+105,t3*penis+105)
        '''
        kit.servo[0].angle = t1*penis+105
        kit.servo[1].angle = t2*penis+105
        kit.servo[2].angle = t3*penis+105
        kit.servo[4].angle = t1*penis+105
        kit.servo[5].angle = t2*penis+105
        kit.servo[6].angle = t3*penis+105
        kit.servo[8].angle = t1*penis+105
        kit.servo[9].angle = t2*penis+105
        kit.servo[10].angle= t3*penis+105'''
    for i in range (80,-80,-1):
        t1, t2, t3 = botti.delta_calcInverse(-20,i/4,-125)
        botti.move_all_a(t1*penis+105,t2*penis+105,t3*penis+105)
        '''
        kit.servo[0].angle = t1*penis+105
        kit.servo[1].angle = t2*penis+105
        kit.servo[2].angle = t3*penis+105
        kit.servo[4].angle = t1*penis+105
        kit.servo[5].angle = t2*penis+105
        kit.servo[6].angle = t3*penis+105
        kit.servo[8].angle = t1*penis+105
        kit.servo[9].angle = t2*penis+105
        kit.servo[10].angle= t3*penis+105
        '''
    for i in range (-80,80,1):
        t1, t2, t3 = botti.delta_calcInverse(i/4,-20,-125)
        botti.move_all_a(t1*penis+105,t2*penis+105,t3*penis+105)
        '''
        kit.servo[0].angle = t1*penis+105
        kit.servo[1].angle = t2*penis+105
        kit.servo[2].angle = t3*penis+105
        kit.servo[4].angle = t1*penis+105
        kit.servo[5].angle = t2*penis+105
        kit.servo[6].angle = t3*penis+105
        kit.servo[8].angle = t1*penis+105
        kit.servo[9].angle = t2*penis+105
        kit.servo[10].angle= t3*penis+105'''
    for i in range (-80,80,1):
        t1, t2, t3 = botti.delta_calcInverse(20,i/4,-125)
        botti.move_all_a(t1*penis+105,t2*penis+105,t3*penis+105)
        '''
        kit.servo[0].angle = t1*penis+105
        kit.servo[1].angle = t2*penis+105
        kit.servo[2].angle = t3*penis+105
        kit.servo[4].angle = t1*penis+105
        kit.servo[5].angle = t2*penis+105
        kit.servo[6].angle = t3*penis+105
        kit.servo[8].angle = t1*penis+105
        kit.servo[9].angle = t2*penis+105
        kit.servo[10].angle= t3*penis+105
'''