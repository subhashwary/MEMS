import serial
import time

for baud in [9600, 19200, 38400, 57600, 115200]:

    try:
        print("\n====================")
        print("Testing baud:", baud)

        ser = serial.Serial(
            port="COM5",
            baudrate=baud,
            timeout=2
        )

        time.sleep(2)

        ser.write(b"*IDN?\n")

        time.sleep(1)

        response = ser.readline()

        print("Response:", response)

        ser.close()

    except Exception as e:
        print("Error:", e)
