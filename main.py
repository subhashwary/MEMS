import serial
import time

ser = serial.Serial("COM5", 9600, timeout=2)

commands = [
    "VSET1:5.0\n",
    "ISET1:0.5\n",
    "OUT1\n"
]

for cmd in commands:

    print("Sending:", cmd.strip())

    ser.write(cmd.encode())

    time.sleep(1)

    print("Waiting:", ser.in_waiting)

    if ser.in_waiting:
        print("Response:", ser.read_all())

ser.close()
