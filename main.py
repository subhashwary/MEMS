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
