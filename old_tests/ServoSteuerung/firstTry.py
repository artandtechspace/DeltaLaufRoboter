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
        print("Starte ", self.iD)
        for i in range(10):
            posi = input("Auf welcher Position soll der Servo stehen?")
            if int(posi) < 0 or int(posi) > 120:
                print("Bitte gebe eine Zahl zwischen 0 und 120 ein.")
            elif int(posi) <= int(120) and int(posi) >= 0:
                kit.servo[self.iD].angle = int(posi)
                C = open('datenC', 'w')
                C.write(str(posi))
                C.close()
                time.sleep(1)
            else:
                print("Fehler")

            time.sleep(0.1)
        print("Beende ", self.iD)

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

t1 = Fred(1, "t1")
t2 = Fred(2, "t2")

#t1.start()
t2.start()