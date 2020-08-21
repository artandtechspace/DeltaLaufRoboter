from Bot import groupA, groupB
from time import sleep

def s(pos):
    print(pos)
    sleep(5)

#Rotation | Extend | Height

#Default position
groupA.moveRot(0,0,100)
groupB.moveRot(0,0,100)
s("Default position")

#A up
groupA.moveRot(0,0,0)
s("A up")

#B backward
groupB.moveRot(50,100,100)
s("B back")

#A down forward
groupA.moveRot(0,100,100)
s("A down")

#B up
groupB.moveRot(0,0,0)
s("B up")

#A back
groupA.moveRot(50,100,100)
s("A back")

#B forward
groupB.moveRot(0,100,100)
s("B forward")
