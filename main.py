import serial
import time

ser = serial.Serial(
    "COM5",
    baudrate=9600,
    timeout=2
)

for cmd in [
    "VSET1:2.00\r\n",
    "ISET1:0.10\r\n",
    "OUT1\r\n"
]:
    print("Sending:", repr(cmd))
    ser.write(cmd.encode())
    time.sleep(1)

ser.close()

print("Done")
