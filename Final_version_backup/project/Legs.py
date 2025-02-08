from adafruit_servokit import ServoKit

#Maximale range für die Servos
MAX_RANGE = 120

#Min and max value für die servos
MIN = 40
MAX = 120

#Ob das Modul bereits gestartet wurde
isInited = False

'''
    Startet beide Beingruppen (Servokits)
'''
def init(channels=16,g1Address=0x40,g2Adress=0x60):
    global isInited
    if not isInited:
        isInited=True
        global G1
        global G2
        #Creates the servos
        G1 = ServoKit(channels=channels, address=g1Address)
        G2 = ServoKit(channels=channels, address=g2Adress)
        
        #Sets the servo ranges
        _initServo(0,G1)
        _initServo(4,G1)
        _initServo(8,G1)

        _initServo(0,G2)
        _initServo(4,G2)
        _initServo(8,G2)

'''
    Startet die Beingruppe 
'''
def _initServo(rotor,group):
    group.servo[rotor].actuation_range = MAX_RANGE  #Set actuation range of Servo 0 to MAX_RANGE
    group.servo[rotor+1].actuation_range = MAX_RANGE  #Set actuation range of Servo 1 to MAX_RANGE
    group.servo[rotor+2].actuation_range = MAX_RANGE  #Set actuation range of Servo 2 to MAX_RANGE
    
    
'''
    Bewegt ein ganzes Bein
'''
def move(α,β,γ,rotor,group):
    group.servo[rotor].angle = α
    group.servo[rotor+1].angle = β
    group.servo[rotor+2].angle = γ
    
    
'''
    Bewegt alle Beine (Beide Gruppen) gleich
'''
def moveAll(α,β,γ):
    move(α,β,γ,0,G1)
    move(α,β,γ,4,G1)
    move(α,β,γ,8,G1)
    move(α,β,γ,0,G2)
    move(α,β,γ,4,G2)
    move(α,β,γ,8,G2)