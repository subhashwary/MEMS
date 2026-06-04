# detect_protocol.py

import serial
import time

ser = serial.Serial("COM5", 9600, timeout=1)

for i in range(20):

    data = ser.read(100)

    if data:
        print(data)

    time.sleep(0.5)

ser.close()
