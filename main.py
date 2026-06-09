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


this is detect_instruments.py

import serial.tools.list_ports

print("\nAvailable COM Ports:\n")

ports = serial.tools.list_ports.comports()

if len(ports) == 0:
    print("No COM ports detected.")

else:
    for port in ports:
        print(f"Port: {port.device}")
        print(f"Description: {port.description}")
        print(f"HWID: {port.hwid}")
        print("-" * 40)


this above is find_ports.py

import csv
import os
from datetime import datetime

CSV_FILE = "sensor_data.csv"


def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Timestamp",
                "Pressure_kPa",
                "DMM_Voltage",
                "PSU_Voltage",
                "PSU_Current",
                "Mode"
            ])


def log_data(pressure, dmm_voltage, psu_voltage, psu_current, mode):
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            pressure,
            dmm_voltage,
            psu_voltage,
            psu_current,
            mode
        ])



this is logger.py
