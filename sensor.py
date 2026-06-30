if psu and system_state["psu_output"]:

    try:

        with psu_lock:
            psu.write("OUT0")
            time.sleep(0.2)

        system_state["psu_output"] = False
        system_state["psu_voltage"] = 0.0
        system_state["psu_current"] = 0.0

        print(f"Cycle {cycle_no} PSU OFF")

    except Exception as e:

        print("PSU OFF ERROR:", e)
