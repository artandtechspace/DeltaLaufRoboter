from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x40)
kid = ServoKit(channels=16, address=0x60)
import time
import DeltaLaufRoboter as botti

StartPunkt = [85, 86, 85, 100, 103, 107, 110, 100, 84, 85, 86]
StardPunkt = [75, 80, 72, 100, 77, 80, 76, 100, 84, 81, 81]
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

kit.servo[0].actuation_range = 120 
kit.servo[1].actuation_range = 120  
kit.servo[2].actuation_range = 120

kid.servo[0].actuation_range = 120 
kid.servo[1].actuation_range = 120  
kid.servo[2].actuation_range = 120

bla = 20
blie = 30
'''
  
x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))
    
a1,a2,a3 = botti.delta_calcInverse(x,y,z)
    
    #a1+=180
    #a2+=180
    #a3+=180
print("A1: "+str(a1)+" A2: "+str(a2)+" A3: "+str(a3)+"\
kit.servo[0].angle = a1*-1+15
kit.servo[1].angle = a2*-1+15
kit.servo[2].angle = a3*-1+15
'''

while True:
    '''
    a1,a2,a3 = botti.delta_calcInverse(0,0,-255)
    kit.servo[0].angle = a1*-1+105
    kit.servo[1].angle = a2*-1+105
    kit.servo[2].angle = a3*-1+105
    time.sleep(1)
    
    b1,b2,b3 = botti.delta_calcInverse(0,0,-290)
    kit.servo[0].angle = b1*-1+105
    kit.servo[1].angle = b2*-1+105
    kit.servo[2].angle = b3*-1+105
    time.sleep(1)
    
    c1, c2, c3 = botti.delta_calcInverse(0, 0, -300)
    kit.servo[0].angle = c1*-1+105
    kit.servo[1].angle = c2*-1+105
    kit.servo[2].angle = c3*-1+105   
    
    time.sleep(1)
    
   
    
    for i in range(-50,50,1):
        b1,b2,b3 = botti.delta_calcInverse(i,0,-269)
        kit.servo[0].angle = b1*-1+105
        kit.servo[1].angle = b2*-1+105
        kit.servo[2].angle = b3*-1+105
        time.sleep(0.05)
        
    time.sleep(1)
    
    d1, d2, d3 = botti.delta_calcInverse(50, 0, -255)
    kit.servo[0].angle = d1*-1+105
    kit.servo[1].angle = d2*-1+105
    kit.servo[2].angle = d3*-1+105
    
    time.sleep(
    for i in range(0, 800s, 1):
        x = i/10
        if x != 0:
            m = (-269+255)/(x*x)   #m für Stauchung bzw Streckung
        else:
            m = 0.1
        z = (m*x*x)-265
        a1, a2, a3 = botti.delta_calcInverse(x, 0, z)
        kit.servo[0].angle = a1*-1+105
        kit.servo[1].angle = a2*-1+105
        kit.servo[2].angle = a3*-1+105
        time.sleep(0.01)

    for i in range(800 ,0, -1):
        x = i/10
        if x != 0:
            m = (-269+255)/(x*x)   #m für Stauchung bzw Streckung
        else:
            m = 0.1
        z = (m*x*x)-255
        a1, a2, a3 = botti.delta_calcInverse(x, 0, z)
        kit.servo[0].angle = a1*-1+105
        kit.servo[1].angle = a2*-1+105
        kit.servo[2].angle = a3*-1+105
        time.sleep(0.01)
        
        
    
    
    botti.Parabel(80, 80, -300,0.02)
    for i in range (800,-800,-1):
        t1, t2, t3 = botti.delta_calcInverse(i/10,i/10,-300)
        kit.servo[0].angle = t1*-1+105
        kit.servo[1].angle = t2*-1+105
        kit.servo[2].angle = t3*-1+105
        time.sleep(0.001)
    botti.ParabelInv(-80, -80, -300, 0.02)
    '''
    for i in range(11):
        kit.servo[i].angle = bla*-1 + StartPunkt[i]
        kid.servo[i].angle = bla*-1 + StardPunkt[i]
    time.sleep(1)
    for i in range(11):
        kit.servo[i].angle = blie*-1 + StartPunkt[i]
        kid.servo[i].angle = blie*-1 + StardPunkt[i]
    time.sleep(1)