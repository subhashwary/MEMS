import pyvisa

rm = pyvisa.ResourceManager()

psu = rm.open_resource("ASRL5::INSTR")
