import random
import serial
import time

#com = serial.Serial('/dev/ttyUSB0', 9600)
com = serial.Serial('/dev/pts/4', 9600)

ser = serial.Serial()
ser.port = '/dev/pts/4'
serial.timeout = 1
serial.writeTimeout = .29
serial.open()
serial.flushInput()


random.seed(2345)

while True:
    com.writelines("test")
    time.sleep(.3)