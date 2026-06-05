import serial
import time

ser = serial.Serial(
    "COM5",
    9600,
    timeout=5
)

time.sleep(5)

print("Waiting:", ser.in_waiting)

if ser.in_waiting:
    print(ser.read_all())

ser.close()
