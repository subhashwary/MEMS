from instrument import PowerSupply
import time

psu = PowerSupply("COM5", 9600)

print(psu.query("VSET1?"))
print(psu.query("ISET1?"))

psu.output_on()

time.sleep(1)

print(psu.query("VOUT1?"))
print(psu.query("IOUT1?"))

psu.close()
