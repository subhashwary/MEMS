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

import serial
import time

from threading import Lock

serial_lock = Lock()

class SCPIInstrument:

    def __init__(self, port, baudrate=115200, timeout=2):

        self.port = port

        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=timeout
        )

        time.sleep(1)

    # -------------------------------------------------
    # WRITE COMMAND
    # -------------------------------------------------
    def write(self, cmd):

        if not cmd.endswith("\n"):
            cmd += "\n"

        self.ser.write(cmd.encode())

    # -------------------------------------------------
    # QUERY COMMAND
    # -------------------------------------------------
    def query(self, cmd):

        with serial_lock:

            try:
                # Clear old data
                self.ser.reset_input_buffer()
                self.ser.reset_output_buffer()

                # Add newline automatically
                if not cmd.endswith("\n"):
                    cmd += "\n"

                # Send command
                self.ser.write(cmd.encode())

                # Wait for full response
                time.sleep(0.3)

                # Read response
                response = self.ser.readline().decode(
                    errors='ignore'
                ).strip()

                print(f"SCPI QUERY [{cmd.strip()}] -> {response}")

                return response

            except Exception as e:

                print("SCPI Query Error:", e)

                return "ERROR"

    # -------------------------------------------------
    # CLOSE PORT
    # -------------------------------------------------
    def close(self):

        if self.ser.is_open:
            self.ser.close()


# =====================================================
# POWER SUPPLY CLASS
# =====================================================

class PowerSupply(SCPIInstrument):

    def idn(self):
        return self.query("*IDN?")

    def set_voltage(self, voltage):
        self.write(f"VSET1:{voltage}")

    def set_current(self, current):
        self.write(f"ISET1:{current}")

    def get_voltage(self):
        return self.query("VOUT1?")

    def get_current(self):
        return self.query("IOUT1?")

    def output_on(self):
        self.write("OUT1")

    def output_off(self):
        self.write("OUT0")


# =====================================================
# MULTIMETER CLASS
# =====================================================

class Multimeter(SCPIInstrument):

    def idn(self):

        return self.query("*IDN?")

    def measure_voltage(self):

        try:
            with serial_lock:

                # Clear old garbage data
                self.ser.reset_input_buffer()

                # Send command
                self.ser.write(b"MEAS:VOLT:DC?\n")

                # Small wait for full response
                time.sleep(0.2)

                # Read full line
                response = self.ser.readline().decode(errors='ignore').strip()

                print("RAW RESPONSE:", response)

                # Clean unwanted characters
                response = response.replace('\r', '').replace('\n', '')

                # Reject incomplete scientific notation
                if response.endswith('E') or response.endswith('+') or response.endswith('-'):
                    raise ValueError(f"Incomplete reading: {response}")

                value = float(response)

                return round(value, 4)

        except Exception as e:

            print("Measurement Error:", e)

            return None


from instrument import Multimeter
import time

# CONNECT TO DMM
dmm = Multimeter("COM3")

# PRINT DMM ID
print("DMM ID:")
print(dmm.idn())

print("\nReading Voltage...\n")

while True:

    voltage = dmm.measure_voltage()

    print("Voltage =", voltage, "V")

    time.sleep(1)


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
