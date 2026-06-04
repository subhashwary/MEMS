import serial
import time

ser = serial.Serial("COM5", 9600, timeout=2)

time.sleep(2)

print("Sending 2V")

ser.write(b"VSET1:2.00\n")

time.sleep(1)

print("Done")

ser.close()
