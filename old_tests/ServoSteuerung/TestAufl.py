from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time
import DeltaLaufRoboter as botti

kit.servo[0].actuation_range = 120 
kit.servo[1].actuation_range = 120  
kit.servo[2].actuation_range = 120

while True:
    for i in range(3000):
         kit.servo[0].angle = i/100
         time.sleep(0.0003)
