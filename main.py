import serial

ser = serial.Serial(
    "COM5",
    9600,
    timeout=1
)

print("CTS =", ser.cts)
print("DSR =", ser.dsr)
print("RI  =", ser.ri)
print("CD  =", ser.cd)

ser.close()
