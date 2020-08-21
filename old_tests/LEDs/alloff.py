import board
import neopixel
pixels = neopixel.NeoPixel(board.D18,72)


r=0
g=0
b=0
for p in range(len(pixels)):
    pixels[p] = (r,g,b)
