import serial
import time

ser = serial.Serial("COM5", 9600, timeout=2)

commands = [
    b"VSET1:2.00\r\n",
    b"VSET 2.00\r\n",
    b"SOURCE:VOLT 2.00\r\n"
]

for cmd in commands:
    print("Sending:", cmd)
    ser.write(cmd)
    time.sleep(3)

input("Watch PSU display. Did any command change the voltage?")
ser.close()
