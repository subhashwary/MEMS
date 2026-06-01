import serial
import time

ports = ["COM5", "COM6", "COM11", "COM12"]

for port in ports:
    try:
        ser = serial.Serial(port, baudrate=9600, timeout=2)
        time.sleep(1)

        ser.write(b"*IDN?\n")
        time.sleep(0.5)

        response = ser.readline().decode(errors='ignore').strip()

        print(f"{port}: {response if response else 'No response'}")
        ser.close()

    except Exception as e:
        print(f"{port}: Not available ({e})")
