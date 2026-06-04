import serial
import time

ser = serial.Serial("COM5", 9600, timeout=1)

while True:
    cmd = input("Send command: ")

    ser.write((cmd + "\r\n").encode())

    time.sleep(1)

    data = ser.read_all()

    print("Response:", data)
