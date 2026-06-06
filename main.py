psu.write(f"VSET1:{voltage:.3f}\n")
psu.write(f"ISET1:{current:.3f}\n")
psu.write("OUT1\n")
