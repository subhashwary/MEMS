import serial
import time

ser = serial.Serial("COM5", 9600, timeout=2)

tests = [
    "VSET1?\n",
    "ISET1?\n",
    "VOUT1?\n",
    "IOUT1?\n",
    "STATUS?\n",
    "*IDN?\n",

    "VSET1?\r",
    "ISET1?\r",
    "VOUT1?\r",
    "IOUT1?\r",

    "VSET1?\r\n",
    "ISET1?\r\n",
    "VOUT1?\r\n",
    "IOUT1?\r\n",
]

for cmd in tests:

    print("\nTEST:", repr(cmd))

    ser.reset_input_buffer()

    ser.write(cmd.encode())

    time.sleep(1)

    print("waiting:", ser.in_waiting)

    data = ser.read_all()

    print("response:", data)

ser.close()
