from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)

kit.servo[0].actuation_range =120

kit.servo[0].angle = 120
time.sleep(2)
print("120")
   
kit.servo[0].angle = 60
time.sleep(2)
print("60")
    
kit.servo[0].angle = 0
time.sleep(2)
print("0")

kit.servo[0].angle = 60
time.sleep(2)
print("60")
    
kit.servo[0].angle = 120
time.sleep(2)
print("120")
   
kit.servo[0].angle = 60
time.sleep(2)
print("60")
    
kit.servo[0].angle = 0
time.sleep(2)
print("0")

kit.servo[0].angle = 60
time.sleep(2)
print("60")
    
print("fi")
time.sleep(5)
    
while True:
    kit.servo[0].angle = 120
    time.sleep(2)
    print("120")
   
    kit.servo[0].angle = 60
    time.sleep(2)
    print("60")
    
    kit.servo[0].angle = 0
    time.sleep(2)
    print("0")

    kit.servo[0].angle = 60
    time.sleep(2)
    print("60")