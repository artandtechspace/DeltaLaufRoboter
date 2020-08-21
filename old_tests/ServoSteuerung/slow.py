from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

import threading
import time

kit.servo[0].actuation_range = 120  #Set actuation range of Servo 0 to 120
kit.servo[1].actuation_range = 120  #Set actuation range of Servo 2 to 120
kit.servo[2].actuation_range = 120  #Set actuation range of Servo 2 to 120

class Fred(threading.Thread):
    def __init__(self, iD, name):
        threading.Thread.__init__(self)
        self.iD = iD
        self.name = name
    def run(self):
        for i in range(30,60,1):
            kit.servo[self.iD].angle = i
            if self.iD == 0:
                A = open('datenA', 'w')
                A.write(str(i))
                A.close()
            elif self.iD == 1:
                B = open('datenB', 'w')
                B.write(str(i))
                B.close()
            elif self.iD == 2:
                C = open('datenC', 'w')
                C.write(str(i))
                C.close()
            time.sleep(0.01)
        for i in range(60,30,-1):
            kit.servo[self.iD].angle = i
            if self.iD == 0:
                A = open('datenA', 'w')
                A.write(str(i))
                A.close()
            elif self.iD == 1:
                B = open('datenB', 'w')
                B.write(str(i))
                B.close()
            elif self.iD == 2:
                C = open('datenC', 'w')
                C.write(str(i))
                C.close()
            time.sleep(0.01)

def letzte_Position():
    A = open('datenA', 'r')
    adaten = A.read()
    A.close
    kit.servo[0].angle = int(adaten)

    B = open('datenB', 'r')
    bdaten = B.read()
    B.close
    kit.servo[1].angle = int(bdaten)

    C = open('datenC', 'r')
    cdaten = C.read()
    C.close
    kit.servo[2].angle = int(cdaten)
    
letzte_Position()

#t0 = Fred(0, "t0")
#t1 = Fred(1, "t1")
#t2 = Fred(2, "t2")

#t0.start()
#t1.start()
#t2.start()