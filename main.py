import serial
import time

ser = serial.Serial(
    port="COM5",
    baudrate=9600,
    timeout=2
)

time.sleep(1)

commands = [
    "VSET1?",
    "ISET1?",
    "STATUS?",
]

for cmd in commands:

    print("\nSending:", cmd)

    ser.reset_input_buffer()

    ser.write((cmd + "\r\n").encode())

    time.sleep(1)

    data = ser.read(200)

    print("HEX:", data.hex())
    print("RAW:", data)

ser.close()
