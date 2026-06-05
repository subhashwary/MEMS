(venv) PS D:\Wary\MEMS> mode COM5

Status for device COM5:
-----------------------
    Baud:            9600
    Parity:          None
    Data Bits:       8
    Stop Bits:       1
    Timeout:         ON
    XON/XOFF:        OFF
    CTS handshaking: OFF
    DSR handshaking: OFF
    DSR sensitivity: OFF
    DTR circuit:     ON
    RTS circuit:     ON


import serial
import time

for baud in [9600, 19200, 38400, 57600, 115200]:

    print("\nTesting", baud)

    try:

        ser = serial.Serial(
            "COM5",
            baudrate=baud,
            timeout=2
        )

        time.sleep(1)

        ser.write(b"*IDN?\n")

        time.sleep(1)

        print("Waiting:", ser.in_waiting)

        print("Received:", ser.read_all())

        ser.close()

    except Exception as e:

        print(e)
