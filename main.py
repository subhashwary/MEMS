from instrument import Multimeter
import time

dmm = Multimeter("COM3")

print("Connected:")
print(dmm.idn())

print("\nReading voltage...\n")

while True:

    voltage = dmm.measure_voltage()

    print("Voltage =", voltage)

    time.sleep(1)
