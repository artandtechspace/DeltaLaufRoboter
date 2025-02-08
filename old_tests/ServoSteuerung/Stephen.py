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
stepwidth = 30
stepheight = -150
delaytime = 0
trolol = 35

def stephen(gruppe,gruppe2):
    for n in range(trolol):
        time.sleep(delaytime)
        botti.moveInv(-stepwidth,0,stepheight+n,gruppe)
        botti.moveInv(-stepwidth,0,stepheight+n,gruppe2)
    for i in range(-stepwidth,stepwidth,1):
        time.sleep(delaytime)
        botti.moveInv(i,0,stepheight+trolol,gruppe)
        botti.moveInv(i,0,stepheight+trolol,gruppe2)
    for n in range(trolol):
        time.sleep(delaytime)
        botti.moveInv(stepwidth,0,stepheight+trolol-n,gruppe)
        botti.moveInv(stepwidth,0,stepheight+trolol-n,gruppe2)
for i in range(16):
    kit.servo[i].actuation_range = 120
    kid.servo[i].actuation_range = 120
    
botti.moveInv_all(-50,0,stepheight)

while True:
    #botti.moveInv_all(0,0,-125)
    #botti.moveInv(0,0,-200,0)
    
    stephen(0,4)
    stephen(1,5)
    stephen(2,3)
    for i in range(stepwidth,-stepwidth,-1):
        botti.moveInv_all(i,0,stepheight)
        time.sleep(delaytime)