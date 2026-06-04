import serial
import time

ser = serial.Serial(
    port="COM5",
    baudrate=9600,
    timeout=2
)

time.sleep(2)

commands = [
    "VSET1:2.00\n",
    "VSET1 2.00\n",
    "VSET1=2.00\n"
]

for cmd in commands:

    print("Sending:", cmd.strip())

    ser.write(cmd.encode())

    time.sleep(3)

input("Check PSU display. Press ENTER...")

ser.close()
