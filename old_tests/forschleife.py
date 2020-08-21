from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)

kit.servo[1].actuation_range =120

kit.servo[1].angle = 60
time.sleep(3)

for i in range(0, 1200, 1):
    kit.servo[1].angle = i/10
    time.sleep(0.1)

for i in range(1200, 0, -1):
    kit.servo[1].angle = i/10
    time.sleep(0.1)