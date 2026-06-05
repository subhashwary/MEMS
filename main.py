if psu:
    try:

        v = psu.get_voltage()
        i = psu.get_current()

        if v:
            system_state["psu_voltage"] = float(v)

        if i:
            system_state["psu_current"] = float(i)

    except Exception as e:

        print("PSU read error:", e)
