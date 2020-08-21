from evdev import list_devices, InputDevice, categorize, ecodes

from adafruit_servokit import ServoKit
groupA = ServoKit(channels=16,address=0x40)
groupB = ServoKit(channels=16,address=0x60)
import time
import DeltaLaufRoboter as botti
import threading

for i in range(16):
    groupA.servo[i].actuation_range = 120
    groupB.servo[i].actuation_range = 120 

class Bot(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.x = 0
        self.y = 0
        self.z = -150
        self.__res__()
    
    def __res__(self):
        self.preX = self.x
        self.preY = self.y
        self.preZ = self.z
    
    def run(self):        
        botXB,botYB,botZB = botti.delta_calcInverse(0,0,-120)
        groupB.servo[0].angle = botXB*2+30
        groupB.servo[1].angle = botYB*2+30
        groupB.servo[2].angle = botZB*2+30
        groupB.servo[4].angle = botXB*2+30
        groupB.servo[5].angle = botYB*2+30
        groupB.servo[6].angle = botZB*2+30
        groupB.servo[8].angle = botXB*2+30
        groupB.servo[9].angle = botYB*2+30
        groupB.servo[10].angle = botZB*2+30
                
        while True:
            time.sleep(0.025)
            if self.x != self.preX or self.y != self.preY or self.z != self.preZ:
                self.__res__()
                botX,botY,botZ = botti.delta_calcInverse(self.x,self.y,self.z)
                
                groupA.servo[0].angle = botX*2+30
                groupA.servo[1].angle = botY*2+30
                groupA.servo[2].angle = botZ*2+30
                groupA.servo[4].angle = botX*2+30
                groupA.servo[5].angle = botY*2+30
                groupA.servo[6].angle = botZ*2+30
                groupA.servo[8].angle = botX*2+30
                groupA.servo[9].angle = botY*2+30
                groupA.servo[10].angle = botZ*2+30
                '''
                groupB.servo[0].angle = botX*-1+81
                groupB.servo[1].angle = botY*-1+86
                groupB.servo[2].angle = botZ*-1+78
                groupB.servo[4].angle = botX*-1+77
                groupB.servo[5].angle = botY*-1+80
                groupB.servo[6].angle = botZ*-1+76
                groupB.servo[8].angle = botX*-1+84
                groupB.servo[9].angle = botY*-1+81
                groupB.servo[10].angle = botZ*-1+81
                '''


groupB.servo[0].angle = 10+30
groupB.servo[1].angle = 10+30
groupB.servo[2].angle = 10+30
groupB.servo[4].angle = 10+30
groupB.servo[5].angle = 10+30
groupB.servo[6].angle = 10+30
groupB.servo[8].angle = 10+30
groupB.servo[9].angle = 10+30
groupB.servo[10].angle = 10+30
bot = Bot()
bot.start()

#Gets the input (Controller)
board = InputDevice(list_devices()[0])

#Waits for controller input
for event in board.read_loop():
    try:
        #Categorizes the 
        absevent = categorize(event)
        #Checks if the event is for the joystick
        if event.type == ecodes.EV_ABS:
            #Checks if the event is for X
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
                val = absevent.event.value/255
                bot.x = val*80-40
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
                val = absevent.event.value/255
                bot.y = val*80-40
        else:
            pass
            #print(event)
    except AttributeError:
        pass