from evdev import list_devices, InputDevice, categorize, ecodes

#Gets the input (Controller)
board = InputDevice(list_devices(0))

#Waits for controller input
for event in board.read_loop():
   #Checks if the event is for the joystick
   if event.type == ecodes.EV_ABS:
	#Checks if the event is for X
	if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
	   
