time.sleep(0.5)

print("VERIFY VOUT =", psu.query("VOUT1?"))
print("VERIFY IOUT =", psu.query("IOUT1?"))
