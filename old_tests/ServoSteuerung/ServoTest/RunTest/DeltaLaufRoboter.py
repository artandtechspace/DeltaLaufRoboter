import math
from adafruit_servokit import ServoKit
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=0x40)
kid = ServoKit(channels=16, address=0x60)
import time
import DeltaLaufRoboter as botti
import Coordutil

StartPunkt = [87, 88, 87, "105", 103, 107, 110, "105", 84, 85, 86, "105", 81, 86, 78, "105", 77, 80, 76, "105", 84, 81, 81]

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

for i in range(16):
    kit.servo[i].actuation_range = 120
    kid.servo[i].actuation_range = 120 

e = 26.12435565
f = 37.7239197
re= 126
rf= 80.5

b = -94                  #Nullpunkt Höhe



sqrt3= math.sqrt(3.0)
pi = 3.1415926
sin120 = sqrt3/2.0
sin120 = sqrt3/2.0
cos120 = -0.5
tan60 = sqrt3
sin30 = 0.5
tan30 = 1.0/sqrt3

def delta_calcAngleYZ(x0,y0,z0):
    y1 = -0.5 * 0.57735 * f   # f/2 * tan(30 deg)
    y0 -= 0.5 * 0.57735 * e   # shift center to edge

    # z = a + b*y
    a = (x0*x0 + y0*y0 + z0*z0 +rf*rf - re*re - y1*y1)/(2.0*z0)
    b = (y1-y0)/z0

    # discriminant
    d = -(a+b*y1)*(a+b*y1)+rf*(b*b*rf+rf);
    if d < 0:
        return [1,0] # non-existing povar.  return error, theta

    yj = (y1 - a*b - math.sqrt(d))/(b*b + 1) # choosing outer povar
    zj = a + b*yj

    temp = 0.0
    if yj > y1:
        temp=180.0

    theta = math.atan(-zj/(y1 - yj)) * 180.0/pi + temp

    return [0,theta]

def delta_calcInverse(x0, y0, z0):
    theta1 = 0;
    theta2 = 0;
    theta3 = 0;
    status = delta_calcAngleYZ(x0, y0, z0)

    if status[0] == 0:
        theta1=status[1]
        status = delta_calcAngleYZ(x0*cos120 + y0*sin120, y0*cos120-x0*sin120, z0)  # rotate coords to +120 deg

    if status[0] == 0:
        theta2=status[1]
        status = delta_calcAngleYZ(x0*cos120 - y0*sin120, y0*cos120+x0*sin120, z0)  # rotate coords to -120 deg

    theta3=status[1]

    return [theta1,theta2,theta3]


def Parabel(x0, y0, z0,servo = 0, zeit = 0.1):
    b = -115
    xy = math.sqrt(x0*x0+y0*y0)
    angle = math.atan(x0/y0)               #Winkel zur x Achse
    coa = math.cos(angle)                  # Cosinus von alpha
    sia = math.sin(angle)                  #sinus vin alpha
    m = (z0-b)/(xy*xy)                     #m = Stauchung bzw Strexkung
    

    ab1, ab2, ab3 = delta_calcInverse(0,0,b)
    kit.servo[servo].angle = ab1*-1+105
    kit.servo[servo+1].angle = ab2*-1+105
    kit.servo[servo+2].angle = ab3*-1+105
    
    for i in range(round(xy)):
        z = m*i*i+b
        y2 = coa*i
        x2 = sia*i
        if x0 < 0:
            x2= x2*-1
        if y0 < 0:
            y2 = y2*-1
        an1, an2, an3 = delta_calcInverse(x2,y2,z)
        kit.servo[0].angle = an1*-1+105
        kit.servo[1].angle = an2*-1+105
        kit.servo[2].angle = an3*-1+105
        time.sleep(zeit)
       
def ParabelInv(x0, y0, z0, zeit = 0.1):
    b = -115
    xy = math.sqrt(x0*x0+y0*y0)
    angle = math.atan(x0/y0)               #Winkel zur x Achse
    coa = math.cos(angle)                  # Cosinus von alpha
    sia = math.sin(angle)                  #sinus vin alpha
    m = (z0-b)/(xy*xy)                     #m = Stauchung bzw Strexkung
    

    
    for i in range(round(xy),0,-1):
        z = m*i*i+b
        y2 = coa*i
        x2 = sia*i
        if x0 < 0:
            x2= x2*-1
        if y0 < 0:
            y2 = y2*-1
        an1, an2, an3 = delta_calcInverse(x2,y2,z)
        kit.servo[0].angle = an1*-1+105
        kit.servo[1].angle = an2*-1+105
        kit.servo[2].angle = an3*-1+105
        time.sleep(zeit)
        
def ParabelAll(x0, y0, z0, zeit = 0.1):
    b = -115
    xy = math.sqrt(x0*x0+y0*y0)
    angle = math.atan(x0/y0)               #Winkel zur x Achse
    coa = math.cos(angle)                  # Cosinus von alpha
    sia = math.sin(angle)                  #sinus vin alpha
    m = (z0-b)/(xy*xy)                     #m = Stauchung bzw Strexkung
    

    ab1, ab2, ab3 = delta_calcInverse(0,0,b)
    bo1, bo2, bo3 = delta_calcInverse(0,0,b)
    
    kit.servo[0].angle = ab1*-1+StartPunkt[0]
    kit.servo[1].angle = ab2*-1+StartPunkt[1]
    kit.servo[2].angle = ab3*-1+StartPunkt[2]
    kit.servo[4].angle = ab1*-1+StartPunkt[4]
    kit.servo[5].angle = ab2*-1+StartPunkt[5]
    kit.servo[6].angle = ab3*-1+StartPunkt[6]
    kit.servo[8].angle = ab1*-1+StartPunkt[8]
    kit.servo[9].angle = ab2*-1+StartPunkt[9]
    kit.servo[10].angle = ab3*-1+StartPunkt[10]
        
    kid.servo[0].angle = bo1*-1+StartPunkt[12]
    kid.servo[1].angle = bo2*-1+StartPunkt[13]
    kid.servo[2].angle = bo3*-1+StartPunkt[14]
    kid.servo[4].angle = bo1*-1+StartPunkt[16]
    kid.servo[5].angle = bo2*-1+StartPunkt[17]
    kid.servo[6].angle = bo3*-1+StartPunkt[18]
    kid.servo[8].angle = bo1*-1+StartPunkt[20]
    kid.servo[9].angle = bo2*-1+StartPunkt[21]
    kid.servo[10].angle= bo3*-1+StartPunkt[22]
    for i in range(round(xy)):
        z = m*i*i+b
        y2 = coa*i
        x2 = sia*i
        if x0 < 0:
            x2= x2*-1
        if y0 < 0:
            y2 = y2*-1
        an1, an2, an3 = delta_calcInverse(x2,y2,z)
        bm1, bm2, bm3 = delta_calcInverse(x2*-1,y2*-1,z)
        try:
            kit.servo[0].angle = an1*-1+StartPunkt[0]
            kit.servo[1].angle = an2*-1+StartPunkt[1]
            kit.servo[2].angle = an3*-1+StartPunkt[2]
            kit.servo[4].angle = an1*-1+StartPunkt[4]
            kit.servo[5].angle = an2*-1+StartPunkt[5]
            kit.servo[6].angle = an3*-1+StartPunkt[6]
            kit.servo[8].angle = an1*-1+StartPunkt[8]
            kit.servo[9].angle = an2*-1+StartPunkt[9]
            kit.servo[10].angle = an3*-1+StartPunkt[10]
            
            kid.servo[0].angle = bm1*-1+StartPunkt[12]
            kid.servo[1].angle = bm2*-1+StartPunkt[13]
            kid.servo[2].angle = bm3*-1+StartPunkt[14]
            kid.servo[4].angle = bm1*-1+StartPunkt[16]
            kid.servo[5].angle = bm2*-1+StartPunkt[17]
            kid.servo[6].angle = bm3*-1+StartPunkt[18]
            kid.servo[8].angle = bm1*-1+StartPunkt[20]
            kid.servo[9].angle = bm2*-1+StartPunkt[21]
            kid.servo[10].angle= bm3*-1+StartPunkt[22]
        except ValueError:
            print("Value Error")
        time.sleep(zeit)
        
       
def ParabelInvAll(x0, y0, z0, zeit = 0.1):
    b = -115
    xy = math.sqrt(x0*x0+y0*y0)
    angle = math.atan(x0/y0)               #Winkel zur x Achse
    coa = math.cos(angle)                  # Cosinus von alpha
    sia = math.sin(angle)                  #sinus vin alpha
    m = (z0-b)/(xy*xy)                     #m = Stauchung bzw Strexkung
    

    
    for i in range(round(xy),0,-1):
        z = m*i*i+b
        y2 = coa*i
        x2 = sia*i
        if x0 < 0:
            x2= x2*-1
        if y0 < 0:
            y2 = y2*-1
        an1, an2, an3 = delta_calcInverse(x2,y2,z)
        bm1, bm2, bm3 = delta_calcInverse(x2*-1,y2*-1,z)
        kit.servo[0].angle = an1*-1+StartPunkt[0]
        kit.servo[1].angle = an2*-1+StartPunkt[1]
        kit.servo[2].angle = an3*-1+StartPunkt[2]
        kit.servo[4].angle = an1*-1+StartPunkt[4]
        kit.servo[5].angle = an2*-1+StartPunkt[5]
        kit.servo[6].angle = an3*-1+StartPunkt[6]
        kit.servo[8].angle = an1*-1+StartPunkt[8]
        kit.servo[9].angle = an2*-1+StartPunkt[9]
        kit.servo[10].angle = an3*-1+StartPunkt[10]
        
        kid.servo[0].angle = bm1*-1+StartPunkt[12]
        kid.servo[1].angle = bm2*-1+StartPunkt[13]
        kid.servo[2].angle = bm3*-1+StartPunkt[14]
        kid.servo[4].angle = bm1*-1+StartPunkt[16]
        kid.servo[5].angle = bm2*-1+StartPunkt[17]
        kid.servo[6].angle = bm3*-1+StartPunkt[18]
        kid.servo[8].angle = bm1*-1+StartPunkt[20]
        kid.servo[9].angle = bm2*-1+StartPunkt[21]
        kid.servo[10].angle= bm3*-1+StartPunkt[22]
        time.sleep(zeit)
    
def moveA(x,y,z):
    x,y,z = Coordutil.portCoords(x,y,z)
    an1, an2, an3 = delta_calcInverse(x,y,z)
    kit.servo[0].angle = an1*-1+StartPunkt[0]
    kit.servo[1].angle = an2*-1+StartPunkt[1]
    kit.servo[2].angle = an3*-1+StartPunkt[2]
    kit.servo[4].angle = an1*-1+StartPunkt[4]
    kit.servo[5].angle = an2*-1+StartPunkt[5]
    kit.servo[6].angle = an3*-1+StartPunkt[6]
    kit.servo[8].angle = an1*-1+StartPunkt[8]
    kit.servo[9].angle = an2*-1+StartPunkt[9]
    kit.servo[10].angle = an3*-1+StartPunkt[10]

def moveB(x,y,z):
    fusch = x < 0 or y < 0
    x,y,z = Coordutil.portCoords(x,y,z)
    bm1, bm2, bm3 = delta_calcInverse(x*-1,y*-1,z)
    kid.servo[0].angle = bm1*-1+StartPunkt[12]
    kid.servo[1].angle = bm2*-1+StartPunkt[13]
    kid.servo[2].angle = bm3*-1+StartPunkt[14]
    kid.servo[4].angle = bm1*-1+StartPunkt[16]
    kid.servo[5].angle = bm2*-1+StartPunkt[17]
    kid.servo[6].angle = bm3*-1+StartPunkt[18]
    kid.servo[8].angle = bm1*-1+StartPunkt[20]
    kid.servo[9].angle = bm2*-1+StartPunkt[21]
    kid.servo[10].angle= bm3*-1+StartPunkt[22]
        
