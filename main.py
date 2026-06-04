import pyvisa

rm = pyvisa.ResourceManager()

print("Available Resources:")
for resource in rm.list_resources():
    print(resource)
