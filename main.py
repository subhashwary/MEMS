# -----------------------------------------------------
# PSU READINGS
# -----------------------------------------------------
if psu:
    try:

        with psu_lock:
            v = psu.get_voltage()
            i = psu.get_current()

        if v not in ["", "ERROR", None]:
            system_state["psu_voltage"] = float(v)

        if i not in ["", "ERROR", None]:
            system_state["psu_current"] = float(i)

    except Exception as e:

        print("PSU read error:", e)
