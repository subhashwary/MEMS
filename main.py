# scan_psu.py

import serial
import time

for baud in [2400,4800,9600,19200,38400,57600,115200]:

    print("\nBAUD =", baud)

    try:
        ser = serial.Serial(
            "COM5",
            baudrate=baud,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1
        )

        time.sleep(2)

        for cmd in [
            b"*IDN?\r\n",
            b"*IDN?\r",
            b"*IDN?\n",
            b"ID?\r\n",
            b"MODEL?\r\n"
        ]:

            print("Sending:", cmd)

            ser.write(cmd)

            time.sleep(1)

            resp = ser.read(100)

            print("Response:", resp)

        ser.close()

    except Exception as e:
        print(e)
