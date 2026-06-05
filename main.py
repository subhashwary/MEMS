try:
    psu = PowerSupply(
        port="COM5",
        baudrate=9600,
        timeout=2
    )

    print("================================")
    print("PSU CONNECTED")
    print("PORT = COM5")
    print("================================")

except Exception as e:

    print("PSU CONNECTION FAILED")
    print(e)

    psu = None

dmm = None
