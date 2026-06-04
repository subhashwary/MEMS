import serial
import time

ser = serial.Serial(
    port="COM5",
    baudrate=9600,
    timeout=1
)

print("Port opened")

while True:

    data = ser.read(100)

    if data:
        print(data)
