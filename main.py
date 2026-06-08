import serial
import time

ser = serial.Serial(
    port="COM5",
    baudrate=9600,
    timeout=2
)

time.sleep(1)

print("Sending commands...")

ser.write(b"VSET1:2.00\r\n")
time.sleep(1)

ser.write(b"ISET1:0.10\r\n")
time.sleep(1)

ser.write(b"OUT1\r\n")

print("Done")

ser.close()
