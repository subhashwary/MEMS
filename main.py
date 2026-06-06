# -----------------------------------------------------
# PSU READINGS (PUT ONLY IN /data ROUTE)
# -----------------------------------------------------

PSU_READ_INTERVAL = 0.3
last_psu_read = system_state.get("last_psu_read", 0)

if psu and (time.time() - last_psu_read > PSU_READ_INTERVAL):

    try:
        with psu_lock:
            v = psu.query("VOUT1?")
            i = psu.query("IOUT1?")

        system_state["psu_voltage"] = parse_value(v)
        system_state["psu_current"] = parse_value(i)

        system_state["last_psu_read"] = time.time()

    except Exception as e:
        print("PSU read error:", e)
