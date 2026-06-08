idn  = candidate.query("*IDN?")
vset = candidate.query("VSET1?")
iset = candidate.query("ISET1?")

print("IDN  =", idn)
print("VSET =", vset)
print("ISET =", iset)

if not idn and not vset and not iset:
    print("No PSU response")
    candidate.close()
    continue
