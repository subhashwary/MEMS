import pyvisa

rm = pyvisa.ResourceManager()

for resource in rm.list_resources():
    try:
        inst = rm.open_resource(resource)
        print(resource, "->", inst.query("*IDN?"))
    except:
        pass
