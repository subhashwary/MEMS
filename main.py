import pyvisa

rm = pyvisa.ResourceManager()

print("Searching...")

for r in rm.list_resources():
    print(r)
