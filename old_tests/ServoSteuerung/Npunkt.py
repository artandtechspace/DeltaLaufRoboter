from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].actuation_range = 120  #Set actuation range of Servo 0 to 120
kit.servo[1].actuation_range = 120  #Set actuation range of Servo 2 to 120
kit.servo[2].actuation_range = 120


a = 105

kit.servo[0].angle = a
kit.servo[1].angle = a
kit.servo[2].angle = a