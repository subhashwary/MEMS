import serial

ser = serial.Serial("COM5", 9600, timeout=2)

ser.write(b"VSET1:2.00\r\n")

ser.close()

print("done")
