import board
import busio
import adafruit_pca9685
import time
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c, address=0x40)

pca.frequency = 50
while True:
        
    led_channel = pca.channels[0]



    #led_channel.duty_cycle = 300

    #time.sleep(0.01)

    led_channel.duty_cycle = 40
    
    #time.sleep(0.01)
