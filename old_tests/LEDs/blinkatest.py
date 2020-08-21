import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18,72)


def sameforall(red, green, blue):
        pixels[i]    = (red, green, blue)
        pixels[i+12] = (red, green, blue)
        pixels[i+24] = (red, green, blue)
        pixels[i+36] = (red, green, blue)
        pixels[i+48] = (red, green, blue)
        pixels[i+60] = (red, green, blue)


while True:
    
    for i in range(12):
        sameforall(200,0,0)
        time.sleep(.005)
    for i in range(12):
        sameforall(0,200,0)
        time.sleep(.005)
    for i in range(12):
        sameforall(0,0,200)
        time.sleep(.005)