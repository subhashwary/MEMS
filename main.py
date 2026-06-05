from instrument import PowerSupply

psu = PowerSupply("COM5", 9600)

psu.write("VSET1:3.0")
print("sent")

input("Check PSU display and press Enter...")
