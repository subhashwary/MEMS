from instrument import PowerSupply

psu = PowerSupply("COM5", 9600)

print("IDN:", psu.query("*IDN?"))
print("VSET:", psu.query("VSET1?"))
print("VOUT:", psu.query("VOUT1?"))
print("STATUS:", psu.query("STATUS?"))

psu.close()
