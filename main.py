import serial
import time

ser = serial.Serial(
    port="COM5",
    baudrate=9600,
    timeout=2
)

time.sleep(2)

print("Sending 2V command...")

ser.write(b"VSET1:2.00\n")

time.sleep(1)

ser.close()

print("Done")
