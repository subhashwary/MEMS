import serial
import time

ser = serial.Serial(
    "COM5",
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=2
)

commands = [
    b"VSET1:2.00\r\n",
    b"VSET1:2.00\r",
    b"VSET1:2.00\n",
]

for cmd in commands:
    print("Sending:", cmd)
    ser.write(cmd)
    time.sleep(3)

ser.close()
