from evdev import InputDevice, categorize, ecodes
import time
import turtle




gamepad = InputDevice('/dev/input/event6')
t = turtle.Turtle()
screen = t.getscreen()
while True:
    t.forward(2)
    for event in gamepad.read_loop():
        if event.code == 3:
            print(str(event.value) + "    " + str(event.type))
            if event.value <= 127:
                t.left(event.value-128)
            elif event.value >= 128:
                t.right (event.value-128)
