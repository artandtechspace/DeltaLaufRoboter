from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event2')

for event in gamepad.read_loop():
    if event.code == 1:
        print(event)
    if event.code!= 0 and event.code >= 300:
        print(event)

    
