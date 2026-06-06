psu.write("VOUT1?\r\n")
v = psu.read().strip()

psu.write("IOUT1?\r\n")
i = psu.read().strip()
