from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time
import DeltaLaufRoboter as botti

import board

import busio

import adafruit_pca9685

i2c = busio.I2C(board.SCL, board.SDA)

pca = adafruit_pca9685.PCA9685(i2c)
