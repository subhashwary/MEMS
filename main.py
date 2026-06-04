from instrument import Multimeter

print("Connecting to COM3...")

dmm = Multimeter("COM3")

print("DMM ID:")
print(dmm.idn())
