try:

    psu = PowerSupply(
        port="COM6",   # replace with actual PSU port
        baudrate=9600,
        timeout=2
    )

    print("================================")
    print("PSU CONNECTED")
    print(psu.idn())
    print("================================")

except Exception as e:

    print("PSU CONNECTION FAILED")
    print(e)

    psu = None
