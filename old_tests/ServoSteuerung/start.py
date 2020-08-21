import pickle
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].actuation_range = 120
kit.servo[1].actuation_range = 120
kit.servo[2].actuation_range = 120

a = 60 
b = 60
c = 60

kit.servo[0].angle = a
A = open('datenA', 'w')
A.write(str(a))
A.close()

kit.servo[1].angle = b
B = open('datenB', 'w')
B.write(str(b))
B.close()

kit.servo[2].angle = c
C = open('datenC', 'w')
C.write(str(c))
C.close()

A = open('datenA', 'r')
ad = A.read()
A.close
print(int(ad))