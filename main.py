import serial
import time

psu = serial.Serial("COM5", 9600, timeout=1)

psu.write(b"*IDN?\r\n")
time.sleep(0.2)
print(psu.readline())
