if psu and not system_state["psu_output"]:

    try:

        voltage = system_state["config"]["voltage"]
        current = system_state["config"]["current"]

        with psu_lock:

            psu.write(f"VSET1:{voltage:.3f}")
            time.sleep(0.2)

            psu.write(f"ISET1:{current:.3f}")
            time.sleep(0.2)

            psu.write("OUT1")
            time.sleep(0.2)

        system_state["psu_output"] = True
        system_state["psu_voltage"] = voltage
        system_state["psu_current"] = current

        print(f"Cycle {cycle_no}: PSU ON")
        print(f"Voltage = {voltage} V")
        print(f"Current = {current} A")

    except Exception as e:

        print("PSU ON ERROR:", e)
