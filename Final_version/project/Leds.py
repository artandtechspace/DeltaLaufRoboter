import board
import neopixel

#Ob das Modul bereits gestartet wurde
isInited = False

#global var pixels | Speichert die array-referenz für alle leds

'''
    Startet das Led modul des Roboters
    @param port der Port auf welchem die Led's angesteuert werden. Default = board.D18
    @param amount anzahl der Led's welche am roboter vorhanden sind. Default = 72
'''
def init(amount = 72,port = board.D18):
    global isInited
    if not isInited:
        isInited=True
        global pixels
        pixels = neopixel.NeoPixel(port,amount)
    
'''
    Setzt die angegebene Led farbe für alle Pixel ausgehen von der @param(led)
'''
def setForAll(red, green, blue):
    for i in range(len(pixels)):
        pixels[i]=(red,green,blue)
        

'''
    Sets für jedes Led-Rad (Ausgehen von 6a12) die farbe.
'''
def setForAllWheels(led, red, green, blue):
    pixels[led]    = (red, green, blue)
    pixels[led+12] = (red, green, blue)
    pixels[led+24] = (red, green, blue)
    pixels[led+36] = (red, green, blue)
    pixels[led+48] = (red, green, blue)
    
'''
    Sets die Farbe für eine LED
'''
def set(led, red, green, blue):
    pixels[led] = (red,green,blue)