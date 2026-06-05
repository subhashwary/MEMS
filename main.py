print("\nTesting PSU...")

print("IDN =", psu.query("*IDN?"))
print("VSET =", psu.query("VSET1?"))
print("ISET =", psu.query("ISET1?"))
