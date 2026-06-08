import serial
import time

for port in ["COM3", "COM5"]:

    print("\n===================")
    print("Testing", port)

    try:
        ser = serial.Serial(
            port,
            baudrate=9600,
            timeout=2
        )

        ser.write(b"VSET1?\n")

        time.sleep(1)

        data = ser.read(100)

        print("Received:", data)

        ser.close()

    except Exception as e:
        print(e)
