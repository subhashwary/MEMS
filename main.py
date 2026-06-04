import serial
import time

ser = serial.Serial(
    port="COM5",
    baudrate=9600,
    timeout=2
)

while True:

    cmd = input("Command: ")

    if cmd.lower() == "exit":
        break

    ser.write((cmd + "\r\n").encode())

    time.sleep(1)

    data = ser.read_all()

    print("Response:", data)

ser.close()
