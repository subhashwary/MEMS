from instrument import PowerSupply

psu = PowerSupply(
    port="COM5",
    baudrate=9600,
    timeout=2
)

print("Testing...")

psu.set_voltage(5.0)
psu.set_current(0.5)

input("Press Enter to turn ON")

psu.output_on()

print("DONE")
