import pyvisa

rm = pyvisa.ResourceManager()

print(rm.list_resources())

psu = rm.open_resource("ASRL5::INSTR")

psu.timeout = 5000

try:
    print("Trying *IDN?")
    print(psu.query("*IDN?"))
except Exception as e:
    print("IDN ERROR:", e)

try:
    print("Trying VSET1?")
    print(psu.query("VSET1?"))
except Exception as e:
    print("VSET ERROR:", e)

psu.close()
