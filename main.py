try:

    response = ""

    for baud in [9600, 19200, 38400, 57600]:

        try:

            print(f"\nTrying PSU baudrate: {baud}")

            psu = PowerSupply(
                port=com_port,
                baudrate=baud,
                timeout=2
            )

            print("IDN =", psu.query("*IDN?"))
            print("VSET =", psu.query("VSET1?"))
            print("ISET =", psu.query("ISET1?"))

            response = psu.query("*IDN?")

            if response:
                print(f"SUCCESS at {baud}")
                break

        except Exception as e:

            print(f"Failed at {baud}: {e}")
