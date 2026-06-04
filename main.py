import serial
import time

ser = serial.Serial(
    "COM5",
    baudrate=9600,
    timeout=2
)

time.sleep(2)

ser.write(b"*IDN?\n")

time.sleep(1)

print(ser.readline())

ser.close()
