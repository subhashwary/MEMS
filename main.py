from instrument import PowerSupply

psu = PowerSupply(
    port="COM5",
    baudrate=9600
)

print(psu.query("*IDN?"))
print(psu.query("VSET1?"))
print(psu.query("ISET1?"))
print(psu.query("VOUT1?"))
print(psu.query("IOUT1?"))
