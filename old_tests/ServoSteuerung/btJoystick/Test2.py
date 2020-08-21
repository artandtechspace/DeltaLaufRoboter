#import evdev
from evdev import InputDevice, categorize, ecodes

#cree un objet gamepad | creates object gamepad
gamepad = InputDevice('/dev/input/event2')

#affiche la liste des device connectes | prints out device info at start
print(gamepad)

aBtn = 289
bBtn = 290
xBtn = 288
yBtn = 291
lBtn = 292
rBtn = 293
selBtn = 296
staBtn = 297

#affiche les codes interceptes |  display codes
for event in gamepad.read_loop():
    #Boutons | buttons 
    if event.type == ecodes.EV_KEY:
        #print(event)
        if event.value == 1:
            if event.code == xBtn:
                print("X")
            elif event.code == bBtn:
                print("B")
            elif event.code == aBtn:
                print("A")
            elif event.code == yBtn:
                print("Y")
            elif event.code == lBtn:
                print("LEFT")
            elif event.code == rBtn:
                print("RIGHT")
            elif event.code == selBtn:
                print("Select")
            elif event.code == staBtn:
                print("Start")
        elif event.value == 0:
          print("Relache | Release")

    #Gamepad analogique | Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
             print("Val X: "+str(absevent.event.value))
 #       elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
#             print("Val Y: "+str(absevent.event.value))
