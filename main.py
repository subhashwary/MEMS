import serial
import time

ser = serial.Serial(
    "COM5",
    9600,
    timeout=2
)

print("Connected to COM5")

print("DTR =", ser.dtr)
print("RTS =", ser.rts)

ser.dtr = False
ser.rts = False

print("DTR OFF")
print("RTS OFF")

time.sleep(1)

ser.write(b"*IDN?\r\n")

time.sleep(1)

print("Waiting:", ser.in_waiting)

data = ser.read_all()

print("Received:", data)

ser.close()
