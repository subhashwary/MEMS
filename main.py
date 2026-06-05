from instrument import PowerSupply

psu = PowerSupply(
    port="COM5",
    baudrate=9600,
    timeout=2
)

psu.set_voltage(1.0)

psu.set_current(0.1)

psu.output_on()

print("DONE")
