import math

#Written by Noah | Projektlabor Rheine | projektlabor.org

#Takes coord from -50 - 50 (Percentual) and maps them on the robots system (-40 to 40 and -120 to -180)
#Returns the actuall coords
def portCoords(x,y,z):
    #Coords for x,y are in -40 to 40
    #Coords for z are in -120 to -180
    
    #Settings for jonas (X is for x and y axis)
    minX = -40
    maxX = 40
    minZ = -120
    maxZ = -170

    #Calculates the new x
    nX = (maxX-minX)*(x/100+.5)+minX

    #Calculates the new y
    nY = (maxX-minX)*(y/100+.5)+minX

    #Calculates the new z
    nZ = (maxZ-minZ)*(z/100)+minZ

    #Returns the calculated coordinates
    return (nX,nY,nZ)

#Given are coordinates x and y. It returns tooth coordinates rotated by the given degrees (0-360)
def addDegrees(x,y,deg):
    if x == 0:
        x = 0.1
    if y == 0:
        y = 0.1
        
    if x < -40:
        x = -40
    if x > 40:
        x = 40
    if y < -40:
        y = -40
    if y > 40:
        y = 40
    #Calculates the tan for alpha
    tanA = y/x
    
    #Calculates alpha
    alpha = math.atan(tanA)

    #Adds the degrees to alpha
    alpha+=deg/360*math.pi*2

    #Calculates the hypotenuse
    hypotenuse = math.sqrt(x**2+y**2)

    #returns an array with the coordinates
    return {
        math.cos(alpha)*hypotenuse,
        math.sin(alpha)*hypotenuse
    }
